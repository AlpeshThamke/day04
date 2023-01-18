#This code is for ssh using class approach

data = {}
imp_data= {}

class user:
    def __init__(self, name,email,password):
        """Takes 3 args and make a new user for ssh
        Args:
            Name of type String
            Email of type String
            Password of type String
        """

        first_name,at_the_rate,domain = email.partition('@')

        if (first_name=='') or (at_the_rate=='') or (domain==''):
                raise ValueError("Please provide correct email id")
        if name is None:
            raise ValueError("Name cannot be empty")
        if password is None:
            raise ValueError("Passwords cannot be empty")
        
        if email in data:
            raise ValueError("email id  already present")
            
        self._name = name
        self._key = email
        self._password = password
        data[self._key] = [name,password]
        self._logs = []
        print("User {} created with {} as key".format(name,email))


    def user_details(self):
        return self._name,self._key



    def change_password(self,key,old_pswd,new_pswd):
        if key not in data:
            raise ValueError("key does not exist")

        if data[key]==old_pswd:
            data[key]=new_pswd
            self._password = new_pswd
        else:
            raise ValueError("Old Password does not match")



    def log_in(self,key,password):
        border = "-"*50
        print("You are logged in")
        turns = 1
        while True:
            if turns%2==1:
                print(border)
                print("{}'s Terminal/Server".format(self._name))
                print("To know your account details type 'user_details'")
                print("To log out from server type 'log_out'")
                print("To print user log type 'log_data'")
                print("To know available servers type 'servers'")
                print("To connect your server with other server type 'start_SSH'")

                datas = input()
                self._logs.append("{} >>> {}".format(self._name,datas))
                if datas == "user_details":
                    user_name=self._name
                    user_key = self._key
                    print("Your Name: {}".format(user_name))
                    print("Your key: {}".format(user_key))
                
                if datas == "log_out":
                    main()

                if datas == "log_data":
                    print("okay printing log data...")
                    for i,v in enumerate(self._logs):
                        print("{}. {}".format(i+1,v))
                
                if datas == 'servers':
                    all_servers = []
                    for i,v in data.items():
                        all_servers.append(i)

                    print("All servers -----")
                    for index,items in enumerate(all_servers):
                        na,_,dom = items.partition("@")
                        print("{}. {}".format(index+1,na))

                if datas =="start_SSH":
                        print("Available Options:")
                        all_servers = []
                        for i,v in data.items():
                            if i!=self._key:
                                all_servers.append(i)

                        for index,items in enumerate(all_servers):
                            na,_,dom = items.partition("@")
                            print("{}. {}".format(index+1,na))

                        print("Type the name of the server and it's key separated by space")
                        text = input()
                        server_name,_,server_key = text.partition(' ')
                        if server_key not in imp_data:
                            print("Invalid Credentials")
                        else:
                            flag = 1
                            print(border)
                            print("Connection Established with {}'s Server/Terminal".format(server_name))
                            self._logs.append("{} >>> You made a ssh connection with {}'s server".format(self._name,server_name))
                            imp_data[server_key]._logs.append("connection success with other server".format(server_name))
                            while flag:
                                print("To add to other server type anything")
                                print("To remove connection type 'end_SSH'")
                                print("To print log of {}'s server type 'log_data'".format(server_name))

                                inp = input()

                                if inp == 'log_data':
                                    print("Printing log data")
                                    for items in imp_data[server_key]._logs:
                                        print(items)
                                    print(border)
                                
                                elif inp=='end_SSH':
                                    imp_data[server_key]._logs.append("{} terminated the connection with your server".format(self._name))
                                    self._logs.append("{} >>> You termincated the ssh connection with {}'s server".format(self._name,server_name))
                                    flag = 0

                                else:
                                    imp_data[server_key]._logs.append("{} >>> {}".format(self._name,inp))

                
            

    def log_out():
        print("logged out");
        main()

     
def main():
    print("Type 1 for making a new account\nType 2 for login into account\nType 3 for changing password for existing account\nPress Ctrl+D to stop this portal")
    val = int(input())
    try:
        val = int(val)

        if val==1:
            print("Your name")
            name = input()
            print("Email ID")
            email = input()
            print("Password")
            password = input()

            try:
                imp_data[email]=user(name,email,password)
                imp_data[email].log_in(email,password);
            except ValueError as e:
                print(str(e))

        elif val==2:
            print("Enter key")
            key = input()
            print("Enter password")
            password = input()
            if key not in data:
                raise ValueError("key does not exits")

            if data[key][1]==password:
                print("Login Successful")
                imp_data[key].log_in(key,password);
            else:
                raise ValueError("Login Failed");


        elif val==3:
            print("Enter Key")
            key = input()
            print("old password")
            old_pswd = input()
            print("New Password")
            new_pswd = input()

            imp_data[key].change_password(key,old_pswd,new_pswd)

    except:
        raise ValueError("Please enter proper input")


if __name__ == '__main__':
    main()
