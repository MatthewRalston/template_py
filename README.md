# README

Make new scripts with expanded logging features and project setup. Personal CLI configuration preferences.

## Install



```bash
pip install . # Installs the configurator module/command to site-packages
mkdir myproject && cd myproject
configurator cli PROJECTNAME # New cli application with module named PROJECTNAME
# OR
configurator fastapi PROJECTNAME # New fastapi application using MatthewRalston/fastapi_template
```

Creates a new directory and CLI app named 'PROJECTNAME'.

There are 5 main files: `appmap.py`, `config.py`, `__init__.py`, `logger.py` and `util.py`.


There is configurable expanded help messages, usage statements, parameter descriptions etc. in the optional `appmap` module. The `config.py` file contains all main constant/variable/global configurations and variables. Use the following to print the semantic version of the program, for instance.

```python
from myapp import config
print(config.VERSION)
```


<!-- Advanced: Describe parameters, inputs, argparse variables, etc. by copy/pasting versions of the `COMMAND_1_PARAMS`, `command_1_usage` and other variables in `appmap.py`, and adjusting the `ALL_PARAMS`, `ALL_INPUTS`, `ALL_FEATURES`, and `ALL_STEPS` constants. These are used to associate the subcommands listed in `config.py` under the `subcommands` and `subcommand_functions` variables. These are mapped (whatever) or unpacked to the variables named 'command_1_name', 'command_2_name', etc. that are used to reference specific subcommand param, inputs, features, and steps during expanded usage/help messages. Parameters, inputs, features, and steps are metadata typically collected by the advanced error handling facilities (optional, in `appmap.py`) and are collected by the exit gracefully command that wraps the entire main/cli functions, and is invoked by default, disabled by the `--debug` flag. Control the released portion of the logs with the `--log-lines` parameter. Useful for large n or the dimension and size in bytes of the data structures involved in your program. -->



## But I don't want any of this!

Delete `appmap.py` and rewrite the 'cli' function of `__init__.py` without the appmap features. Create a normal entry point function using argparse and your own logging, and enjoy!


## FAQ

**Q: Frequently asked question?**

A: Answer to the question.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Matt Ralston - [Website](https://matthewralston.github.io/) - professional.bio.coder@gmail.com

Project Link: [https://github.com/YourUsername/template_py](https://github.com/username/template_py)

## Acknowledgements

- [Library/Resource 1](https://example.com)
- [Library/Resource 2](https://example.com)
- [Library/Resource 3](https://example.com)



<!--
Thanks of course to my fans (and haters). Yeah i see you.... but i dont.
Thanks to my former mentors Andrew S, Charles T, Brian C, Mark R, Isaac N, Carlos R, and my newer bosses Punita J and Kyle L.
Thanks to the Pap lab for the first dataset that I continue to use.
Thank you to Ryan for the food and stuff. I actually made this project specifically so you and I could converse...
Thanks to Blahah for tolerating someone snooping and imitating his Ruby style.
Thanks to Erin for getting my feet wet in this new field. You are my mvp.
Thanks to Rachel for the good memories and friendship. And Sophie too. veggies n' R love.
Thanks to Yasmeen for the usual banter.
Thanks to A for the newer banter.
Thanks to Max, Robin, and Robert for the good memories in St. Louis. What's new?
Thanks to Fred for the good memories. Hope you're on soon.
Thanks to Nichole for the cookies and good memories. And your cute furballs too! Hope you're well
Thanks to S for the lessons, convos, and even embarassing moments. You're kind of awesome to me.
Thanks to a few friends I met in 2023 that reminded me I have a lot to learn about friendship, dating, and street smarts.
Thanks to them even more now that I got it xd up.

Thanks to the people of NCC for the Doordash money. It might not be much but I don't have it twisted (I do.)



Thanks to D from BCCS.
Thanks to C4H&H. I'm 'healthier' now, but I really still think I need more support than just BCCS. it's urgent.
Thanks to CT and family. Your love and support means the world to me.
Thanks to AS and family. Your support made a difference. Praying for better employment and opportunities.

And thanks to my family and friends.
Go Blue Hens
-->
