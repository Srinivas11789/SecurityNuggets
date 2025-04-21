import os 

# Template for the Java class with a placeholder for the comment/payload
FILE_TEMPLATE = """public class Main {
    // %s
    public static void main(String[] args) {
        System.out.println("Hello from main()");
    }
}
"""

# Get user input directly as the payload for the static block
user_code = input("Enter the code you want to insert into the static block: ")

# Directly insert the user input into the template and write to the file
with open('/tmp/Main.java', 'w') as f:
    f.write(FILE_TEMPLATE % user_code)

print(os.system('cat /tmp/Main.java'))