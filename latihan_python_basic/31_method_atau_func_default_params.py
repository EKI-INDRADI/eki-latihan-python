# Belajar Default Argument Value

def say_hello(first_name="Budi", last_name=""):
    print(f"Hello {first_name} - {last_name}")

say_hello("Eki")
say_hello("Indradi", "Eki")
say_hello(last_name="Indradi", first_name="Eki")
say_hello( first_name="Eki2" ,last_name="Indradi2")