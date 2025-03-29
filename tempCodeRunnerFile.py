def student(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
    
d=student(name="Gaurav ad",id="1",grade="bachlor")
