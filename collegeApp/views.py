from django.shortcuts import redirect, render
from collegeApp.models import Course, Student,Tutor,Profile
from django.contrib.auth.models import User,auth
from django.contrib import messages

def add_course(request):
    if "uid" in request.session:
        if request.method == 'POST':
            course = request.POST['course']
            fee = request.POST['fee']
            add = Course(course_name=course,course_fee=fee)
            add.save()
            return redirect('add_course')
        return render(request,'add_course.html',{})
    return redirect(log_in)

def add_student(request):
    if "uid" in request.session:
        tutor = Tutor.objects.all()
        student = Student.objects.all()
        context = {'tutor':tutor,'student':student}
        if request.method == 'POST':
            fname = request.POST['fname']
            lname = request.POST['lname']
            address = request.POST['address']
            age = request.POST['age']
            jdate = request.POST['jdate']
            tut = request.POST['tutor']
            t = Tutor.objects.get(id=tut)
            student = Student(student_first_name=fname,student_last_name=lname,student_address=address,student_age=age,student_joined=jdate,tutor=t)
            student.save()
            return redirect(show_student)
        return render(request,'add_student.html',context)
    return redirect(log_in)

def add_tutor(request):
    if "uid" in request.session:
        course = Course.objects.all()
        if request.method == 'POST':
                tname = request.POST['tutor_name']
                course = request.POST['course']
                c = Course.objects.get(id=course)
                tut = Tutor(tutor_name=tname,course=c)
                tut.save()
                return redirect(add_tutor)
        return render(request,'add_tutor.html',{'course':course})
    return redirect(log_in)


def sign_up(request):
    students = Student.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        fl_name = Student.objects.get(id=name)
        a = request.POST['address']
        address = Student.objects.get(id=a)
        uname = request.POST['username']
        email = request.POST['email']
        passw = request.POST['password']
        cpassw = request.POST['c_password']
        gender = request.POST['gender']
        mobile = request.POST['mobile']
        if passw == cpassw:
                if User.objects.filter(username=uname).exists():
                    messages.info(request, 'username already exists...!')
                    return redirect(sign_up)
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'email already exists...!')
                    return redirect(sign_up)
                else:
                    user = User.objects.create_user(first_name=fl_name.student_first_name,last_name=fl_name.student_last_name,username=uname,email=email,password=passw)
                    user.save()
                    u = User.objects.get(id=user.id)
                    profile = Profile(gender=gender,mobile=mobile,student=fl_name,user=u,address=address.student_address)
                    profile.save()
                    return redirect(log_in)
        else:
            messages.info(request,"Oops...! password doesn't match..!")
            return redirect(sign_up)
    context = {'students':students}
    return render(request,'signup.html',context)

def log_in(request):
    if request.method == 'POST':
        uname = request.POST['username']
        passw = request.POST['password']
        user = auth.authenticate(username=uname,password=passw)
        request.session["uid"] = user.id
        if user is not None:
            auth.login(request,user)
            return redirect(home)
        else:
            messages.info(request,'Invalid username or password...!')
            return redirect(log_in)
    return render(request,'login.html',{})

def log_out(request):
    request.session["uid"] = ""
    auth.logout(request)
    return redirect(log_in)

def home(request):
    if "uid" in request.session:
        return render(request,'home.html',{})
    return redirect(log_in)

def show_student(request):
    if "uid" in request.session:
        students = Student.objects.all()
        return render(request,'show_student.html',{'students':students})
    return redirect(log_in)

def show_tutor(request):
    if "uid" in request.session:
        tutors = Tutor.objects.all()
        return render(request,'show_tutor.html',{'tutors':tutors})
    return redirect(log_in)


def show_course(request):
    if "uid" in request.session:
        courses = Course.objects.all()
        return render(request,'show_course.html',{'courses':courses})
    return redirect(log_in)

def student_details(request,pk):
    if "uid" in request.session:
        details = Student.objects.get(id=pk)
        return render(request,'student_details.html',{'details':details})
    return redirect(log_in)

def edit_student(request,pk):
    student = Student.objects.get(id=pk)
    tutor = Tutor.objects.all()
    if request.method == 'POST':
        student.student_first_name = request.POST['fname']
        student.student_last_name = request.POST['lname']
        student.student_address = request.POST['address']
        student.student_age = request.POST['age']
        student.student_joined = request.POST['jdate']
        tut = request.POST['tutor']
        student.tutor = Tutor.objects.get(id=tut)
        student.save()
        return redirect(show_student)
    return render(request,'edit_student.html',{'student':student,'tutor':tutor})

def delete_student(request,pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect(show_student)

def edit_tutor(request,pk):
    tutor = Tutor.objects.get(id=pk)
    course = Course.objects.all()
    context = {'tutor':tutor,'course':course}
    if request.method == 'POST':
        tutor.tutor_name = request.POST['tutor_name']
        c = request.POST['course']
        tutor.course = Course.objects.get(id=c)
        tutor.save()
        return redirect(show_tutor)
    return render(request,'edit_tutor.html',context)

def delete_tutor(request,pk):
    tutor = Tutor.objects.get(id=pk)
    tutor.delete()
    return redirect(show_tutor)


def edit_course(request,pk):
    course = Course.objects.get(id=pk)
    context = {'course':course}
    if request.method == 'POST':
        course.course_name = request.POST['course']
        course.course_fee = request.POST['fee']
        course.save()
        return redirect(show_course)
    return render(request,'edit_course.html',context)

def delete_course(request,pk):
    course = Course.objects.get(id=pk)
    course.delete()
    return redirect(show_course)

        


