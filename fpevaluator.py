import sys, script

python_sloc_fp = 53.33
python_hours_fp = 9

java_sloc_fp = 53.33
java_hours_fp = 10.6

javascript_sloc_fp = 70
javascript_hours_fp = 10

go_sloc_fp = 53.33
go_hours_fp = 5

csharp_sloc_fp = 51.20
csharp_hours_fp = 15.5

perl_sloc_fp = 35.56
perl_hours_fp = 8

php_sloc_fp = 53.33
php_hours_fp = 12

dotnet_sloc_fp = 24.62
dotnet_hours_fp = 11

html_sloc_fp = 160
html_hours_fp = 4

c_sloc_fp = 128
c_hours_fp = 13

cpp_sloc_fp = 53.33
cpp_hours_fp = 12.4

sql_sloc_fp = 35
sql_hours_fp = 8

xml_sloc_fp = 128
xml_hours_fp = 13

ruby_sloc_fp = 45.71

length = int(len(script.x))

total_function_points = 0
total_man_hours = 0

for i in range(0,length,2):

    lang = script.x[i]
    slocs = script.x[i + 1]

    sloc = int(slocs,10)
    div_fac = 27
    mul_fac = 3
    j = 0.45
    power = mul_fac * j

    function_points = 0
    hours = 0

    if lang == "python":
        function_points = sloc / python_sloc_fp
        hours = function_points * python_hours_fp
    elif lang == "java":
        function_points = sloc / java_sloc_fp
        hours = function_points * java_hours_fp
    elif lang == "JavaScript":
        function_points = sloc / javascript_sloc_fp
        hours = function_points * javascript_hours_fp
    elif lang == "go":
        function_points = sloc / go_sloc_fp
        hours = function_points * go_hours_fp
    elif lang == "csharp":
        function_points = sloc / csharp_sloc_fp
        hours = function_points * csharp_hours_fp
    elif lang == "perl":
        function_points = sloc / perl_sloc_fp
        hours = function_points * perl_hours_fp
    elif lang == "dotnet":
        function_points = sloc / dotnet_sloc_fp
        hours = function_points * dotnet_hours_fp
    elif lang == "HTML":
        function_points = sloc / html_sloc_fp
        hours = function_points * html_hours_fp
    elif lang == "CSS":
        function_points = sloc / html_sloc_fp
        hours = function_points * html_hours_fp
    elif lang == "c":
        function_points = sloc / c_sloc_fp
        hours = function_points * c_hours_fp
    elif lang == "cpp":
        function_points = sloc / cpp_sloc_fp
        hours = function_points * cpp_hours_fp
    elif lang == "sql":
        function_points = sloc / sql_sloc_fp
        hours = function_points * sql_hours_fp
    elif lang == "xml":
        function_points = sloc / xml_sloc_fp
        # hours = function_points * sql_hours_fp
    elif lang == "ruby":
        function_points = sloc / ruby_sloc_fp
        # hours = function_points * sql_hours_fp
    else:
        print("Languages Available and Usage:")
        print("python,java,JavaScript,go,csharp,perl,php,dotnet,HTML,c,cpp,sql,css")


    # print("Hours:", hours/10)
    man_months = function_points ** power 
    man_months = man_months / 27

    print('----------------------------------------')
    print(lang)
    print(sloc)
    print("Function Points:" , function_points)
    print("Man_months:" , man_months)
    print("Man_hours:" , 160 * man_months)
    print('----------------------------------------')

    total_function_points += function_points
    total_man_hours += 160 * man_months

print("Total_function_points:" ,total_function_points)
print("Total_man_hours:" ,total_man_hours)