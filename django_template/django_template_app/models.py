from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator

"""
Django validators

validators.BaseValidator(                          validators.ip_address_validators(
validators.DecimalValidator(                       validators.ipaddress
validators.DomainNameValidator(                    validators.is_valid_ipv6_address(
validators.EMPTY_VALUES                            validators.math
validators.EmailValidator(                         validators.ngettext_lazy(
validators.FileExtensionValidator(                 validators.punycode(
validators.MaxLengthValidator(                     validators.re
validators.MaxValueValidator(                      validators.slug_re
validators.MinLengthValidator(                     validators.slug_unicode_re
validators.MinValueValidator(                      validators.urlsplit(
validators.Path(                                   validators.urlunsplit(
validators.ProhibitNullCharactersValidator(        validators.validate_comma_separated_integer_list(
validators.RegexValidator(                         validators.validate_domain_name(
validators.StepValueValidator(                     validators.validate_email(
validators.URLValidator(                           validators.validate_image_file_extension(
validators.ValidationError(                        validators.validate_integer(
validators.deconstructible(                        validators.validate_ipv46_address(
validators.get_available_image_extensions()        validators.validate_ipv4_address(
validators.int_list_validator(                     validators.validate_ipv6_address(
validators.integer_validator(                      validators.validate_slug(
validators.ip_address_validator_map                validators.validate_unicode_slug(
"""




"""
Django models field


models.Aggregate(                   models.IPAddressField(              models.Sum(
models.AutoField(                   models.ImageField(                  models.TextChoices(
models.Avg(                         models.Index(                       models.TextField(
models.BLANK_CHOICE_DASH            models.IntegerChoices(              models.TimeField(
models.BaseConstraint(              models.IntegerField(                models.Transform(
models.BigAutoField(                models.JSONField(                   models.URLField(
models.BigIntegerField(             models.Lookup(                      models.UUIDField(
models.BinaryField(                 models.Manager(                     models.UniqueConstraint(
models.BooleanField(                models.ManyToManyField(             models.Value(
models.CASCADE(                     models.ManyToManyRel(               models.ValueRange(
models.Case(                        models.ManyToOneRel(                models.Variance(
models.CharField(                   models.Max(                         models.When(
models.CheckConstraint(             models.Min(                         models.Window(
models.Choices(                     models.Model(                       models.WindowFrame(
models.CommaSeparatedIntegerField(  models.NOT_PROVIDED()               models.WindowFrameExclusion(
models.Count(                       models.NullBooleanField(            models.aggregates
models.DEFERRED                     models.ObjectDoesNotExist(          models.aggregates_all
models.DO_NOTHING(                  models.OneToOneField(               models.aprefetch_related_objects(
models.DateField(                   models.OneToOneRel(                 models.base
models.DateTimeField(               models.OrderBy(                     models.constants
models.DecimalField(                models.OrderWrt(                    models.constraints
models.Deferrable(                  models.OuterRef(                    models.constraints_all
models.DurationField(               models.PROTECT(                     models.deletion
models.EmailField(                  models.PositiveBigIntegerField(     models.enums
models.Empty()                      models.PositiveIntegerField(        models.enums_all
models.Exists(                      models.PositiveSmallIntegerField(   models.expressions
models.Expression(                  models.Prefetch(                    models.fields
models.ExpressionList(              models.ProtectedError(              models.fields_all
models.ExpressionWrapper(           models.Q(                           models.functions
models.F(                           models.QuerySet(                    models.indexes
models.Field(                       models.RESTRICT(                    models.indexes_all
models.FileField(                   models.RestrictedError(             models.lookups
models.FilePathField(               models.RowRange(                    models.manager
models.FilteredRelation(            models.SET(                         models.options
models.FloatField(                  models.SET_DEFAULT(                 models.prefetch_related_objects(
models.ForeignKey(                  models.SET_NULL(                    models.query
models.ForeignObject(               models.SlugField(                   models.query_utils
models.ForeignObjectRel(            models.SmallAutoField(              models.signals
models.Func(                        models.SmallIntegerField(           models.sql
models.GeneratedField(              models.StdDev(                      models.utils
models.GenericIPAddressField(       models.Subquery(
"""


# Create your models here.


class User(models.Model):
    """
    Model representing a User with field groups
    """

    class ContactInfo(models.Model):
        email = models.EmailField(
            validators=[EmailValidator()],
            unique=True,
            verbose_name="Contact Email"
        )
        phone = model.CharField(
            max_length=10,
            blank=True,
            null=True,
            verbose_name="Phone Number"
        )
        address = models.CharField(
            max_length=100,
            validators=[MinLengthValidator(5)],
            verbose_name="Address"
        )
        suite = models.CharField(
            max_length=20,
            validators=[MinLengthValidator(0)],
            verbose_name="Suite"
        )
        city = models.CharField(
            max_length=50,
            validators=[MinLengthValidator(3)],
            verbose_name="City"
        )
        state = models.CharField(
            max_length=2,
            validators=[MinLengthValidator(2)],
            verbose_name="State"
        )
        zip_code = models.CharField(
            max_length=5,
            validators=[MinLengthValidator(5)],
            verbose_name="Zip Code"
        )

    class PersonalInfo(models.Model):
        first_name = models.CharField(
            max_length=40,
            validators=[MinLengthValidator(2)],
            verbose_name="First Name"
        )
        last_name = models.CharField(
            max_length=40,
            validators=[MinLengthValidator(2)],
            verbose_name="Last Name"
        )

        company = models.CharField(
            max_length=100,
            validators=[MinLengthValidator(5)],
            verbose_name="Company Name"

    contact = models.OneToOneField(
        ContactInfo,
        on_delete=models.CASCADE,
        realted_name='user_contact'
    )
    personal = models.OneToOneField(
        PersonalInfo,
        on_delete=models.CASCADE,
        related_name='user_personal'
    )
            
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.personal.first_name} {self.personal.last_name}"


class Request(models.Model):

    """
    Model representing a user request with relationships and constraints
    """

    project_name = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(5)],
        verbose_name="Project Name"
    )

    project_description = models.CharField(
        verbose_name="Project Description"
    )
            
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="requests"
    )


    project_submission_date = models.DateTimeField(auto_now_add=True)
    project_due_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name
            

            

            
