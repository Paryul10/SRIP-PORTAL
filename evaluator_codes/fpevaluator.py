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

##############################################################################
comp_org_js = 270.95         #1
comp_org_html = 189.6125
comp_org_css = 59.625

graphics_js = 48.314         #2
graphics_html = 156.03
graphics_css = 28.30

pattern_js = 46.042          #3
pattern_html = 99.443
pattern_css = 28.206


vlsi_js = 726.41            #4
vlsi_html = 298.125
vlsi_css = 62.2565

dld_js = 43.828            #5
dld_html = 144.9625
dld_css = 28.2065


speech_js = 723.4         #6
speech_html = 258.187
speech_css = 32.131
##############################################################################


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
    elif lang == "java":
        function_points = sloc / java_sloc_fp
    elif lang == "JavaScript":
        function_points = sloc / javascript_sloc_fp
        # if script.lab == 1:
        #     function_points = function_points - comp_org_js
        # elif script.lab == 2:
        #     function_points = function_points - graphics_js
        # elif script.lab == 3:
        #     function_points = function_points - pattern_js
        # elif script.lab == 4:
        #     function_points = function_points - vlsi_js
        # elif script.lab == 5:
        #     function_points = function_points - dld_js
        # elif script.lab == 6:
        #     function_points = function_points - speech_js
        # else:
        #     function_points = 0
    elif lang == "go":
        function_points = sloc / go_sloc_fp
    elif lang == "csharp":
        function_points = sloc / csharp_sloc_fp
    elif lang == "perl":
        function_points = sloc / perl_sloc_fp
    elif lang == "dotnet":
        function_points = sloc / dotnet_sloc_fp
    elif lang == "HTML":
        function_points = sloc / html_sloc_fp
        # if script.lab == 1:
        #     function_points = function_points - comp_org_html
        # elif script.lab == 2:
        #     function_points = function_points - graphics_html
        # elif script.lab == 3:
        #     function_points = function_points - pattern_html
        # elif script.lab == 4:
        #     function_points = function_points - vlsi_html
        # elif script.lab == 5:
        #     function_points = function_points - dld_html
        # elif script.lab == 6:
        #     function_points = function_points - speech_html
        # else:
        #     function_points = 0
    elif lang == "CSS":
        function_points = sloc / html_sloc_fp
        # if script.lab == 1:
        #     function_points = function_points - comp_org_css
        # elif script.lab == 2:
        #     function_points = function_points - graphics_css
        # elif script.lab == 3:
        #     function_points = function_points - pattern_css
        # elif script.lab == 4:
        #     function_points = function_points - vlsi_css
        # elif script.lab == 5:
        #     function_points = function_points - dld_css
        # elif script.lab == 6:
        #     function_points = function_points - speech_css
        # else:
        #     function_points = 0
    elif lang == "c":
        function_points = sloc / c_sloc_fp
    elif lang == "cpp":
        function_points = sloc / cpp_sloc_fp
    elif lang == "sql":
        function_points = sloc / sql_sloc_fp
    elif lang == "xml":
        function_points = sloc / xml_sloc_fp
    elif lang == "ruby":
        function_points = sloc / ruby_sloc_fp
    else:
        print("Languages Available and Usage:")
        print("python,java,JavaScript,go,csharp,perl,php,dotnet,HTML,c,cpp,sql,css")

    # if function_points > 0:

    # print("Hours:", hours/10)
    if function_points < 0:
        function_points = 0
    
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