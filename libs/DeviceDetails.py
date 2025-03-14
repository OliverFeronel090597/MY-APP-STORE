import getpass
import socket

def get_user_login():
    return getpass.getuser()

def get_hostname():
    return socket.gethostname()

# # Example usage
# if __name__ == "__main__":
#     print("User Login:", get_user_login())
#     print("Hostname:", get_hostname())
