import sys

lang = sys.argv[1]
slocs = sys.argv[2]

sloc = int(slocs,10)

python_sloc_fp = 20
python_hours_fp = 9

java_sloc_fp = 53
java_hours_fp = 10.6

javascript_sloc_fp = 47
javascript_hours_fp = 10

go_sloc_fp = 18
go_hours_fp = 5

csharp_sloc_fp = 54
csharp_hours_fp = 15.5

perl_sloc_fp = 24
perl_hours_fp = 8

php_sloc_fp = 67
php_hours_fp = 12

dotnet_sloc_fp = 57
dotnet_hours_fp = 11

html_sloc_fp = 15
html_hours_fp = 4

c_sloc_fp = 128
c_hours_fp = 13

cpp_sloc_fp = 53
cpp_hours_fp = 12.4

sql_sloc_fp = 18
sql_hours_fp = 8


function_points = 0
hours = 0

if lang == "python":
    function_points = sloc / python_sloc_fp
    hours = function_points * python_hours_fp
elif lang == "java":
    function_points = sloc / java_sloc_fp
    hours = function_points * java_hours_fp
elif lang == "javascript":
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
elif lang == "html":
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
else:
    print("Languages Available and Usage:")
    print("python,java,javascript,go,csharp,perl,php,dotnet,html,c,cpp,sql")


print("Function Points:" , function_points)
print("Hours:", hours/10)