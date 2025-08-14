from  .models import Schools
from rest_framework import serializers

class updateserializationclass(serializers.ModelSerializer):
    class Meta:
        model=Schools
        fields='__all__'
from .models import lms
from rest_framework import serializers
class stdserializationclass(serializers.ModelSerializer):
    class Meta:
        model=lms
        fields="__all__"

from .models import examcont,examcarl,examcards
from rest_framework import serializers

class serializationclass(serializers.ModelSerializer):
    class Meta:
        model=examcont
        fields='__all__'

class examcarlserializationclass(serializers.ModelSerializer):
    class Meta:
        model=examcarl
        fields='__all__'

class examcardscardsserializationclass(serializers.ModelSerializer):
    class Meta:
        model=examcards
        fields='__all__'
        
from .models import attendmanagecontent,attendmanagecarousel,attendmanagecards
from rest_framework import serializers
class attendmanagementclass1(serializers.ModelSerializer):
    class Meta:
        model=attendmanagecontent
        fields='__all__'
    
class attendmanagementclass2(serializers.ModelSerializer):
    class Meta:
        model=attendmanagecarousel
        fields='__all__'

class attendmanagementclass3(serializers.ModelSerializer):
    class Meta:
        model=attendmanagecards
        fields='__all__'

from .models import admissioncarl,admissioncont,admissioncards
from rest_framework import serializers

class admissioncarlserializationclass(serializers.ModelSerializer):
    class Meta:
        model=admissioncarl
        fields='__all__'

class admissioncontserializationclass(serializers.ModelSerializer):
    class Meta:
        model=admissioncont
        fields='__all__'

class admissioncardsserializationclass(serializers.ModelSerializer):
    class Meta:
        model=admissioncards
        fields='__all__'

from .models import liveclasscontent,liveclasscards,liveclasscarousel
from rest_framework import serializers
class liveclassmanagementclass1(serializers.ModelSerializer):
    class Meta:
        model=liveclasscontent
        fields='__all__'
    


class livemanagementclass2(serializers.ModelSerializer):
    class Meta:
        model=liveclasscarousel
        fields='__all__'
class livemanagementclass3(serializers.ModelSerializer):
    class Meta:
        model=liveclasscards
        fields='__all__'

from .models import timetablecarl,timetablecont,timetablecards
from rest_framework import serializers

class timetablecarlserializationclass(serializers.ModelSerializer):
    class Meta:
        model=admissioncarl
        fields='__all__'

class timetablecontserializationclass(serializers.ModelSerializer):
    class Meta:
        model=admissioncont
        fields='__all__'

class timetablecardsserializationclass(serializers.ModelSerializer):
    class Meta:
        model=admissioncards
        fields='__all__'
