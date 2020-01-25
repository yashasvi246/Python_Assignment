class Contact:
    def __init__(self,p_name,p_no,email_add):
        self.p_name=p_name
        self.p_no=p_no
        self.email_add=email_add
    def get_name(self):
        return input('Enter The Name of The Person')
    def set_name(self):
        self.p_name=self.get_name()
        return self.p_name
    def get_phone(self):
        return input('Enter The Contact Number')
    def set_phone(self):
        self.p_no=self.get_phone()
        return self.p_no
    def get_email(self):
        return input('Enter The E-mail Id of The Person')
    def set_email(self):
        self.email_add=self.get_email()
        return self.email_add
    def insert_record(self):
        contact[self.set_name()]={'phone':self.set_phone(),'email':self.set_email()}
        print(contact)
        print(self.__str__())
        p=input('Do You Want To Store this Record.\nPress 1 To Yes\nPress 2 To No')
        if p=='1':
            with open('contact-dict.txt','a') as f:
                for c, v in contact.items():
                    f.write('name : '+c + '  ')
                    f.write("".join(["  {}: {}".format(v, d) for v, d in v.items()]) + '   ')
                    f.write('\n')
            c=input('Do You Want TO View The Records.\nPress 1 To Yes.\nPress 0 To Exit.\n')
            if c=='1':
                self.display()
            elif c=='0':
                return
            
    def display(self):
        r=open('contact-dict.txt','r')
        p=r.readline()
        while p!='':
            print(p)
            p=r.readline()
    def detail(self):
        per_name=input('Enter the name of the Person')
        r=open('contact-dict.txt','r')
        p=r.readline()
        while p!='':
            if per_name in p:
                print(p)
                break
            else:
                p=r.readline()
    def delete(self):
        per_name=input('Enter the name of the Person whose details you want to delete.')
        with open("contact-dict.txt", "r") as f:
            lines = f.readlines()
            print(lines)
        with open("contact-dict.txt", "w") as f:
            for line in lines:
                if per_name  not in line.strip("\n") :
                    f.write(line)
        
    def update(self):
        per_name=input('Enter the name of the Person whose details you want to update.')
        with open("contact-dict.txt", "r") as f:
            lines = f.readlines()
            
        with open("contact-dict.txt", "w") as f:
            for line in lines:
                if per_name  not in line.strip("\n") :
                    f.write(line)
        self.insert_record()
        
        
        
    
    def __str__(self):
        return f'Person name : {self.p_name}\nPhone : {self.p_no}\nE-mail id : {self.email_add}\n'
def main():
    a=Contact('yashasvi','87090979798','yashasvimahajan276@gmail.com')
    
    while True:
        ch=input('Press 1 to Enter New Record.\nPress 2 to Update Record.\nEnter 3 to View Record.\nPress 4 to get Detail of the person.\nPress 5 to delete Person Detail\nPress 0 to Exit.\n')
        if ch=='1':
            a.insert_record()
        elif ch=='2':
            a.update()
        elif ch=='3':
            a.display()
        elif ch=='4':
            a.detail()
        elif ch=='5':
            a.delete()
            
            
        elif ch=='0':
            break
contact={}
main()
