PLACEHOLDER = "[name]"
        
with open("C:\Python\Python 100 Days\Day 24\Day 24-223\Mail Merge Project Start\Input\Names\invited_names.txt") as names_file:
    names = names_file.readlines()
    
with open("C:\Python\Python 100 Days\Day 24\Day 24-223\Mail Merge Project Start\Input\Letters\starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    
    for name in names:
        strip_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, strip_name)
        with open(f"C:\Python\Python 100 Days\Day 24\Day 24-223\Mail Merge Project Start\Output\ReadyToSend\letter_for_{strip_name}") as competed_letter:
            competed_letter.write(new_letter)