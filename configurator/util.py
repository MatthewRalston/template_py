'''
   Copyright 2020 Matthew Ralston

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

'''


import io
import sys
import os
import gzip
import tempfile
import yaml, json
import re
import shutil
import logging
from collections import deque, OrderedDict

logger = logging.getLogger(__file__)


findall_float = re.compile(r"[-+]?(?:\d*\.\d+|\d+)")


def copy_tree_with_replace(src:str, dst:str, to_replace:str, replace_with:str):
    """
    Copy a directory and contents into a new directory
    """
    if type(src) is not str and not isinstance(src, os.PathLike):
        raise TypeError("configurator.util.replace_during_copy() expects a str as the first positional argument 'src'")
    elif type(dst) is not str and not isinstance(src, os.PathLike):
        raise TypeError("configurator.util.replace_during_copy() expects a str as the second positional argument 'dst'")
    elif type(to_replace) is not str:
        raise TypeError("configurator.util.replace_during_copy() expects a str as the third positional argument 'to_replace'")
    elif type(replace_with) is not str:
        raise TypeError("configurator.util.replace_during_copy() expects a str as the fourth positional argument 'replace_with'")

    curdir = ''
    dstdir = dst

    if not os.path.exists(dst):
        if dst.endswith(to_replace):
            dst = dst.replace(to_replace, replace_with)
        os.mkdir(dst)
            
    
    for dirpath, dirnames, filenames in os.walk(src):
        print("Dirpath:", dirpath)            
        print("Dirnames:", dirnames)
        print("Filenames:", filenames)

        curdir = dst
        
        print("Extracting contents from '{0}' to '{1}'".format(dirpath, dst))
        for fn in filenames:
            src_fname = os.path.join(dirpath, fn)
            if src_fname.count(to_replace) == 2:
                dst_fname = os.path.join(dst, replace_with, fn)
            elif src_fname.count(to_replace) == 1:
                dst_fname = os.path.join(dst,  fn)
            else:
                logger.error("Contents of .tar.gz file extracted to '{0}' were being copied to '{1}'".format(dirpath, dst))
                raise ValueError("Could not determine the nesting structure of the Python source files to be copied.")
            logger.info("Copying from '{0}' to '{1}'".format(src_fname, dst_fname))
            copy_with_replace(src_fname, dst_fname, to_replace=to_replace, replace_with=replace_with)

            
        for dir in dirnames:
            newdir = os.path.join(dst, replace_with) if str(dir).endswith(to_replace) else os.path.join(dst, dir)
            if not os.path.exists(newdir):
                os.mkdir(newdir)
                logger.info("Created directory '{0}'".format(newdir))


        """
        Now copy files
        """
        

def copy_with_replace(src:str, dst:str, to_replace:str=None, replace_with:str=None):
    """
    Replace strings in a file with a different string during shutil.copy2
    """
    if type(src) is not str:
        raise TypeError("configurator.util.copy_with_replace() expects a string as its first positional argument")
    elif type(dst) is not str:
        raise TypeError("configurator.util.copy_with_replace() expects a string as its second positional argument")

    if to_replace is None or type(to_replace) is not str:
        raise TypeError("configurator.util.copy_with_replace() expects the keyword argument 'to_replace' to be a str")
    if replace_with is None or type(replace_with) is not str:
        raise TypeError("configurator.util.copy_with_replace() expects the keyword argument 'replace_with' to be a str")
    
    
    
    if os.path.isdir(src):
        shutil.copy2(src, dst)
    elif os.path.isfile(src):
        # shutil.copy2(src, dst)
        with open(src, 'r') as ifile:
            filedata = ifile.read()
            if filedata.count(to_replace) == 0:
                logger.info("configurator.util.copy_with_replace() did not find any occurrences of '{0}' in the source file '{1}'".format(to_replace, src))
            newdata = filedata.replace(to_replace, replace_with)
            with open(dst, 'w') as ofile:
                ofile.write(newdata)
        
    elif os.path.islink(src):
        shutil.copy2(src, dst)
    else:
        raise ValueError("configurator.util.replace_during_copy() expects the source contents to be a directory, a file, or a symlink.")

def represent_yaml_from_collections_dot_OrderedDict(dumper, data):
    """
    Thanks to Blender and EquipDev on StackOverflow for this handy method to pass to yaml.add_representer
    https://stackoverflow.com/a/16782282

    I use this throughout the metadata representation in the bgzf specification to print out the representer, it's just awesome.

    I really like this answer. Finally got around to liking it this year, in Jan 2022 after using it for like a few years. 

    :param dumper: The OrderedDict_Representer, this faciliatates non-key sorting for optimal metadata block structure.
    :type dumper: 
    :param data:
    :type data: dict
    """

    
    value = []

    for item_key, item_value in data.items():
        node_key = dumper.represent_data(item_key)
        node_value = dumper.represent_data(item_value)

        value.append((node_key, node_value))

    return yaml.nodes.MappingNode(u'tag:yaml.org,2002:map', value)


def is_gz_file(filepath):
    import gzip
    try:
        
        with gzip.open(filepath, 'rb') as f:
            f.readline()
        return True
    except OSError as e:
        return False



def get_histo(counts):
    """
    Get a histogram from an array.
    """

    if type(counts) is not list: # 10/6/24
        raise TypeError("kmerdb.util.get_histo takes a list as its positional argument")
    
    hist = []
    count_max = int(np.max(np.array(counts, dtype="uint64")))

    for i in range(count_max + 1):
        hist.append(0)

    #print("Count max was : {0} from {1} histogram items".format(count_max, len(hist)))    
    #sys.stderr.write("{0} histogram items\n".format(len(hist)))
    for i in range(len(counts)):
        # 10/7/24
        # print("i: {0}".format(i))
        # print("count array length: {0}".format(len(counts)))
        # print("hist array length: {0}".format(len(hist)))
        # print("histogram item: {0}, {1} in {2} histogram items".format(i, counts[i], len(hist)))
        if counts[i] > 2:
            hist[counts[i]] += 1
    return hist



    
def is_all_fasta(filenames):
    """Tests if all the strings in a list are fasta format.
    
    :param filenames:
    :type list:
    :returns bool:
    :rtype bool:
    """
    if type(filenames) is not list:
        raise TypeError("template_py.util.is_all_fasta() expects a list as its first positional argument")
    elif not all(type(s) is str for s in filenames):
        raise TypeError("template_py.util.is_all_fasta() expects a list of str as its first positional argument")
    return all((f.endswith('.fa') or f.endswith('.fasta') or f.endswith('.fa.gz') or f.endswith('.fasta.gz') or f.endswith('.fna') or f.endswith('.fna.gz')) for f in filenames)


def isfloat(num):
    """
    Thanks to the author of:
    https://www.programiz.com/python-programming/examples/check-string-number


    :param num: Check if a string is a float, or could be converted to a float
    :type num: str
    :returns: Whether or not the string can be parsed as a float
    :rtype: bool
    """
    if type(num) is str:
        findall_float.match(num)
        #logger.debug(re.match(findall_float, num))
        return re.match(findall_float, num) is not None
    elif type(num) is float:
        return True
    elif type(num) is int:
        return False
    else:
        #logger.error(type(num))
        #logger.error(num.dtype)
        raise TypeError("template_py.util.isfloat expects a single str as a positional argument")

