***Settings***
Library     String
Library     split.py
Library     auth.py
Library     readfile.py
Library     OperatingSystem

***Variable***
${name}     Firstname MiddleName LastName

***Test Case***
Test 1
    @{var}=     Split String    ${name}     separator=${SPACE}     max_split=1
    Log to console    @{var}[0]

Test 2
    ${a}=   split_var   ${name}
    Log To Console    ${a}

Test 3
    Log File    project.csv    encoding=UTF-8    encoding_errors=strict

Test 4
    ${a}=   read_file       project.csv     Ref Num     Stage
    Log To Console    ${a}

Test 5
    auth_as_superuser    http://tetra-qa.strikersoft.com:8080     Ass2
