import crypt  # Equivalent to the command "openssl passwd" - allows for hashing of password


def main():
    passwords = {
        'jcuser1': 'NyvHCa2.uDaLQ',
        'jcuser2': 'me9XEHaEjGEYU',
        'jcuser3': 'moML07IRIH7rQ',
        'jcuser4': 'ovvViMJBN0bgE',
        'jcuser5': 'plhcPjLZZmOdw',
        'jcuser6': 'inEhxe85IWr3E',
        'jcuser7': 'EvsYMC3LHgAPU',
        'jcuser8': 'whRoVzqe/9wNo',
        'jcuser9': 'hadWRv13WWyV2',
        'jcuser10': 'FiNVGxR5Khi5k'
    }

    for user, password in passwords.items():  # Loop over the user and its password
        salt = password[0:2]  # Get the first two letters of the password
        with open('dictionary') as content:  # Opens the dictionary file
            words = content.readlines()  # Convert the contents of the file into an array
            for word in words:  # Use for loop to iterate over each line
                word = word.rstrip()
                hashed_password = crypt.crypt(word, salt)  # Hashes the word from the dictionary file with a given salt
                if password == hashed_password:  # Check if the password matches the hashed password
                    print "User: %s | Password: %s | Salt: %s | Word: %s" % (user, password, salt, word)

if __name__ == "__main__":
    main()
