import datetime

class Passport:
    """
    Represents a passport with personal information and travel history.

    Attributes:
        passport_counter (int): A class-level counter to assign unique passport IDs.
    """

    passport_counter = 0

    def __init__(self, first_name, last_name, dob, country, exp_date):
        """
        Initializes a Passport instance with the given details.
        :param first_name: First name of the passport holder.
        :param last_name: Last name of the passport holder.
        :param dob: Date of birth in 'YYYY-MM-DD' format.
        :param country: Country of citizenship.
        :param exp_date: Expiration date in 'YYYY-MM-DD' format.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.dob = datetime.date.fromisoformat(dob)
        self.country = country
        self.exp_date = datetime.date.fromisoformat(exp_date)

        self.passport_id = Passport.passport_counter
        Passport.passport_counter += 1

        self.visits = {}

    def summary(self):
        """
        Returns a summary of the passport holder's information, including validity.

        :return str: Summary of the passport holder's information.
        """
        validity = "valid" if self.is_valid() else "invalid"
        return f"This passport belongs to {self.first_name} {self.last_name}, born on {self.dob} in {self.country}, It is {validity}"
    
    def is_valid(self):
        """
        Checks if the passport is currently valid.
        :return bool: True if the passport is valid (expiration date is in the future), False otherwise.
        """
        return self.exp_date > datetime.date.today()
    
    def check_data(self, first_name, last_name, dob, country):
        """
        Check if the given data matches the passport holder's information.
        :param first_name: First name to check.
        :param last_name: Last name to check.
        :param dob: Date of birth in 'YYYY-MM-DD' format to check.
        :param country: Country to check.
        :return bool: True if all provided details match the passport holder's data and the passport is valid.
        """
        return (
            self.first_name == first_name and
            self.last_name == last_name and
            self.dob == datetime.date.fromisoformat(dob) and
            self.country == country and
            self.is_valid()
        )
    
    def stamp(self, country):
        """
        Records a visit to a specified country, updating visit count.
        :param country (str): The country visited.
        """
        if country != self.country:
            if country in self.visits:
                self.visits[country] += 1
            else:
                self.visits[country] = 1

    def countries_visited(self):
        """
        Returns a list of countries visited by the passport holder.

        :return list: List of countries visited.
        """
        return list(self.visits.keys())
    
    def times_visited(self, country):
        """
        Returns the number of the passport holder visited a specified country.
        :param country (str): The country to check.
        :return int: The number of visits to the specified country.
        """
        if country in self.visits:
            return self.visits[country]
        else:
            return 0
        
    def sum_square_visits(self):
        """
        Calculates the sum of squares of visit counts to all visited countries.
        :return int: The sum of squares of visit counts.
        """
        sum_square_visit = 0  
        for count in self.visits.values():
            sum_square_visit += count ** 2 
        return sum_square_visit

    def passport_number(self):
        """
        Returns the unique passport ID.

        :return int: The unique passport ID.
        """
        return self.passport_id





 