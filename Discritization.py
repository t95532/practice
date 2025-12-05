def discretize(data):
    # Discretization (binning) functions for numerical columns
    def discretize_age(age):
        if age < 25:
            return 'Young'
        elif age < 60:
            return 'Adult'
        else:
            return 'Senior'

    def discretize_income(income):
        if income < 25000:
            return 'Low'
        elif income < 100000:
            return 'Medium'
        else:
            return 'High'

    def discretize_emp_length(emp_length):
        if emp_length < 5:
            return 'Short'
        elif emp_length < 10:
            return 'Medium'
        else:
            return 'Long'

    def discretize_loan_amnt(loan_amnt):
        if loan_amnt < 5000:
            return '<5k'
        elif loan_amnt < 10000:
            return '5k-10k'
        elif loan_amnt < 15000:
            return '10k-15k'
        elif loan_amnt < 20000:
            return '15k-20k'
        else:
            return '>20k'

    def discretize_int_rate(int_rate):
        if int_rate < 10:
            return '<10%'
        elif int_rate < 15:
            return '10%-15%'
        elif int_rate < 20:
            return '15%-20%'
        else:
            return '>20%'

    def discretize_percent_income(x):
        if x < 0.3:
            return '<0.3'
        elif x < 0.5:
            return '0.3-0.5'
        else:
            return '>0.5'

    def discretize_cred_hist(x):
        if x < 5:
            return '<5'
        elif x < 10:
            return '5-10'
        else:
            return '>10'

    # Copy dataframe to avoid modifying the original
    df = data.copy()

    # Apply discretization functions to relevant columns
    df['age_group'] = df['person_age'].apply(discretize_age)
    df['income_group'] = df['person_income'].apply(discretize_income)
    df['person_emp_length_group'] = df['person_emp_length'].apply(discretize_emp_length)
    df['loan_amnt_group'] = df['loan_amnt'].apply(discretize_loan_amnt)
    df['loan_int_rate_group'] = df['loan_int_rate'].apply(discretize_int_rate)
    df['loan_percent_income_group'] = df['loan_percent_income'].apply(discretize_percent_income)
    df['cb_person_cred_hist_length_group'] = df['cb_person_cred_hist_length'].apply(discretize_cred_hist)

    return df
