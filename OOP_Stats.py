class Stat_Object:
    
    # this class will create an object containing data points and will allow the user to call statistics or parameters on it
    
    def __init__(self, name, *args,scope='unknown'):
    
        self.name = name # name of dataset
        self.data = args # the dataset
        self.total = len(args) # number of datapoints
        self.scope = 'unknown' # wheter the dataset is a population or a sample
    
    # special methods
    
    def __str__(self):
        return f'{self.name}: {self.data}'
        
    # here are the user-defined methods for the data
    # the 'local' parameter will determine the output of the function i.e. if true it wil output a value, when false it outputs a string
    
    def mean(self,dec=None):
        
        mu = sum(self.data)/self.total
        if dec != None:
            mu = round(mu,dec)
        
        return f'the mean is {mu}'
    
    def median(x,dec=None,local=False):
        
        """return the median of an iterable x
            
            e.g. median([1,2,3]) --> 2"""
        
        if len(x) % 2 == 0:
            i = int(len(x)/2)
            median = (x[i-1]+x[i])/2
        else:
            median = x[int((len(x)-1)/2)]
            
        if dec != None:
            median = round(median,dec)
        return median if local else f'the median of {self.name} is {median}'
    
    def population_variance(self,dec=None,local=False):
    
        mu = sum(self.data)/self.total # calculate the mean and assign to variable
        sq_devs = [(i-mu)**2 for i in self.data] # for each datapoint calculate the deviations, square and store them
        variance = (sum(sq_devs)) / self.total # sum the stored squared deviations and divide by the # of datapoints 
        
        if dec != None:
            variance = round(variance,dec)
        
        return variance if local else f'the population variance for {self.name} is {variance}'

    
    def population_sd(self,dec=None,local=False):
        
        from math import sqrt
        tup = self.data
        
        pop_var = self.population_variance(local=True)
        
        sd = sqrt(pop_var) # take root of population variance
        
        if dec != None:
            sd = round(sd,dec)

        return sd if local == True else f'the population standard deviation for {self.name} is {sd}'
    
    def sample_variance(self,dec=None,local=False):
        
        # calculate the mean and assign to variable
        
        tup = self.data
        
        xbar = sum(tup)/self.total
        
        sq_devs = [(i-xbar)**2 for i in tup] # for each data-point calculate the deviations, square- and store them

        variance = (sum(sq_devs)) / (self.total-1) # sum the stored squared deviations and divide by number of data point
        
        if dec != None:
            variance = round(variance,dec)

        return variance if local else f'the sample variance for {self.name} is {variance}'
    
    def sample_sd(self,dec=None,local=False):
    
        from math import sqrt
        tup = self.data
        
        sample_var = self.sample_variance(local=True)
        
        sd = sqrt(sample_var) # take root of sample variance
        
        if dec != None:
            sd = round(sd,dec)
            
        return sd if local == True else f'the sample standard deviation for {self.name} is {sd}'
    
     def iqr(self,dec=None,local=False): # this method calculates the interquartile range
        
        tup = sorted(self.data)

        if len(tup) % 2 == 0: # if iterable is even
            median = (tup[int(len(tup)/2)] + tup[int(len(tup)/2 -1)])/2 # calculate median 

            first_half = tup[:int(len(tup)/2)] # slice the iterable into first- and second half
            second_half = tup[int(len(tup)/2):]

            if len(first_half) % 2 == 0: # check parity first half
                first_median = (first_half[int(len(first_half)/2)] + first_half[int(len(first_half)/2 -1)])/2 
                second_median = (second_half[int(len(second_half)/2)] + second_half[int(len(second_half)/2 -1)])/2

                IQR = second_median - first_median #calculate IQR
            else:
                first_median = first_half[int(len(first_half)/2-0.5)]
                second_median = second_half[int(len(second_half)/2-0.5)]

                IQR = second_median - first_median

        else: # if iterable is odd
            median = tup[int(len(tup)/2-0.5)]

            first_half = tup[:int(len(tup)/2-0.5)]
            second_half = tup[int(len(tup)/2-0.5 +1):]

            if len(first_half) % 2 == 0: # check parity first half

                first_median = (first_half[int(len(first_half)/2)] + first_half[int(len(first_half)/2 -1)])/2 
                second_median = (second_half[int(len(second_half)/2)] + second_half[int(len(second_half)/2 -1)])/2

                IQR = second_median - first_median 
            else:

                first_median = first_half[int(len(first_half)/2-0.5)]
                second_median = second_half[int(len(second_half)/2-0.5)]

                IQR = second_median - first_median
            
        if dec != None:
                IQR = round(IQR,dec)

        return IQR if local else f'The IQR for {self.name} is {IQR}.'

    def MAD(self,dec=None,local=False): 
        
        # this function calculates the Mean Absolute Deviation
    
        absolute_deviations = []

        mean = sum(self.data)/len(self.data) 

        for data_point in self.data:

            absolute_deviations.append(abs(data_point-mean)) # take absolute deviation for every datapoint

        mad = (sum(absolute_deviations))/self.total # sum them and divide by number of points
        
        if dec != None:
                mad = round(mad,dec)


        return mad if local else f'The MAD for {self.name} is {mad}'
    
    def z_score(self,data_point=0,dec=None,local=False):
    
        scope_range = 'ps'
        scope = ' '
        
        mu = sum(self.data)/self.total
        
        while not scope in scope_range: # ask for user input concerning scope of data
            
            scope = input('Is your data set a Population(p) or a Sample(s)?: ').lower() 
            if not scope in 'ps':
                print('Please enter either p or s.')
        
        if scope == 'p': # save this information about datset in attributes
            self.scope = 'Population' 
        else:
            self.scope = 'Sample'
            
            
        pop_z_score = (data_point - mu)/self.population_sd(local=True) # calculate z-scores
        samp_z_score = (data_point - mu)/self.sample_sd(local=True)
        
        if dec != None:
            pop_z_score = round(pop_z_score,dec)
            samp_z_score = round(samp_z_score,dec)
            
        if local:
            return pop_z_score if scope == 'p' else samp_z_score
        else:
            if scope == 'p':
                return f'The population z-score for point {data_point} is {pop_z_score}'
            else:
                return f'The sample z-score for point {data_point} is {samp_z_score}'
    
