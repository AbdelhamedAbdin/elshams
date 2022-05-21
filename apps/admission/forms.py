from django import forms
from django.core.exceptions import ValidationError
from .models import Admission


STUDENT_CLASS = (
    (1, 'تمهيدى'),
    (2, 'الصف الاول رياض اطفال'),
    (3, 'الصف الثانى رياض اطفال'),
    (4, 'الصف الاول الابتدائى'),
    (5, 'الصف الثانى الابتدائى'),
    (6, 'الصف الثالث الابتدائى'),
    (7, 'الصف الرابع الابتدائى'),
    (8, 'الصف الخامس الابتدائى'),
    (9, 'الصف السادس الابتدائى'),
)

YES_OR_NO = (
    ("YES", "نعم"),
    ("NO", "لا")
)

JOB_NAME = (
    (1, "ربة منزل"),
    (2, "اخرى")
)

QUALIFICATION = (
    ('DB', "الدبلوم"),
    ('BA', "البكالوريوس"),
    ('LI', "ليسانس"),
    ('MJ', "الماجستير"),
    ('DR', "دكتوراه"),
    ('OTHER', "اخرى"),
)


class AdmissionForm(forms.ModelForm):
    class_join = forms.ChoiceField(choices=STUDENT_CLASS, required=True, widget=forms.RadioSelect(), initial=1)
    is_joined_before = forms.ChoiceField(choices=YES_OR_NO, required=True, initial="NO", widget=forms.RadioSelect())

    siblings_count = forms.ChoiceField(choices=YES_OR_NO, required=True, initial="NO", widget=forms.RadioSelect())
    siblings_count_class = forms.ChoiceField(required=False, choices=STUDENT_CLASS, widget=forms.RadioSelect(attrs={'hidden': 'hidden'}),
                                             initial=1)

    mother_job = forms.ChoiceField(choices=JOB_NAME, required=True, initial=1, widget=forms.RadioSelect())
    mother_qualification = forms.ChoiceField(required=True, choices=QUALIFICATION, widget=forms.RadioSelect(), initial='DB')

    father_qualification = forms.ChoiceField(required=True, choices=QUALIFICATION, widget=forms.RadioSelect(), initial='DB')

    class Meta:
        model = Admission
        fields = '__all__'

        widgets = {
            'date': forms.DateInput(attrs={'hidden': 'hidden'}),
            'is_joined_name': forms.TextInput(attrs={'hidden': 'hidden'}),
            'is_joined_duration': forms.TextInput(attrs={'hidden': 'hidden'}),
            'siblings_count_name': forms.TextInput(attrs={'hidden': 'hidden'}),
            'what_mother_job': forms.TextInput(attrs={'hidden': 'hidden'}),
            'mother_qualification_other': forms.TextInput(attrs={'hidden': 'hidden'}),
            'father_qualification_other': forms.TextInput(attrs={'hidden': 'hidden'}),
        }

    def clean_child_name(self):
        form = self.cleaned_data.get("child_name").strip("")

        # force to add 4 name at least
        child_name_count = form.split()
        if len(child_name_count) < 4:
            raise ValidationError("يجب ان يكون الاسم رباعى على الاقل")
        elif len(form) == "":
            raise ValidationError("هذا الحقل مطلوب")
        return form

    def clean_international_id(self):
        form = self.cleaned_data.get("international_id").strip("")
        try:
            if len(form) < 14:
                raise ValidationError("عفوا هذا الحقل يتطلب 14 رقم على الاقل")
            if not isinstance(int(form), int):
                raise ValidationError("هذا الحقل يجب ان يحتوى على ارقام فقط")
        except ValueError:
            raise ValidationError("يوجد خطأ فى العملية حاول مرة اخرى")
        return form

    def clean_is_joined_before(self):
        form = self.cleaned_data.get("is_joined_before")

        if form == "NO":
            form = self.cleaned_data.get("is_joined_before", None)
        return form

    def clean_siblings_count(self):
        form = self.cleaned_data.get("siblings_count")

        if form == "NO":
            form = self.cleaned_data.get("siblings_count", None)
        return form

    def clean(self):
        clean = super().clean()
        mother_phone = clean.get("mother_phone_number")
        father_phone = clean.get("father_phone_number")
        child_name = clean.get("child_name")
        father_name = clean.get("father_name")

        is_joined_before = clean.get("is_joined_before")
        is_joined_name = clean.get("is_joined_name")
        is_joined_duration = clean.get("is_joined_duration")

        siblings_count = clean.get("siblings_count")
        siblings_count_name = clean.get("siblings_count_name")
        siblings_count_class = clean.get("siblings_count_class")

        mother_job = clean.get("mother_job")
        what_mother_job = clean.get("what_mother_job")

        mother_qualification = clean.get("mother_qualification")
        mother_qualification_other = clean.get("mother_qualification_other")

        father_qualification = clean.get("father_qualification")
        father_qualification_other = clean.get("father_qualification_other")

        # prevent the "none field" to request after triggering the option
        if is_joined_before == "YES" and is_joined_name is None:
            error_message = "هذا الحقل مطلوب"
            self.add_error("is_joined_name", error_message)
            raise ValidationError(error_message)

        if is_joined_before == "YES" and is_joined_duration is None:
            error_message = "هذا الحقل مطلوب"
            self.add_error("is_joined_duration", error_message)
            raise ValidationError(error_message)

        if siblings_count == "YES" and siblings_count_name is None:
            error_message = "هذا الحقل مطلوب"
            self.add_error("siblings_count_name", error_message)
            raise ValidationError(error_message)

        if siblings_count == "YES" and siblings_count_class is None:
            error_message = "هذا الحقل مطلوب"
            self.add_error("siblings_count_class", error_message)
            raise ValidationError(error_message)

        if mother_job == 2 and what_mother_job is None:
            error_message = "هذا الحقل مطلوب"
            self.add_error("what_mother_job", error_message)
            raise ValidationError(error_message)

        if mother_qualification == "OTHER" and mother_qualification_other is None:
            error_message = "هذا الحقل مطلوب"
            self.add_error("mother_qualification_other", error_message)
            raise ValidationError(error_message)

        if father_qualification == "OTHER" and father_qualification_other is None:
            error_message = "هذا الحقل مطلوب"
            self.add_error("father_qualification_other", error_message)
            raise ValidationError(error_message)

        try:
            child_father = child_name.split()[1:]
            father = father_name.split()
        except AttributeError:
            child_father = None
            father = father_name

        if child_father != father:
            error_message = "اسم والد الطالب غير مشابه لاسم الاب"
            self.add_error("father_name", error_message)
            raise ValidationError(error_message)

        if mother_phone and father_phone and mother_phone == father_phone:
            error_message = "رقم الاب والام متشابهان من فضلك ادخل رقم غير متشابه"
            self.add_error("mother_phone_number", error_message)
            raise ValidationError(error_message)

    def clean_mother_name(self):
        return self.cleaned_data.get("mother_name").strip("")

    def clean_father_name(self):
        return self.cleaned_data.get("father_name").strip("")
