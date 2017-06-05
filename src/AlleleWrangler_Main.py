# This file is part of Allele-Wrangler.
#
# Allele-Wrangler is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Allele-Wrangler is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Allele-Wrangler. If not, see <http://www.gnu.org/licenses/>.

from AlleleWrangler import AlleleWrangler

# Version 1.0 

SoftwareVersion = "Allele-Wrangler Version 1.0"


import sys
import getopt


def usage():
    print("usage:\n" + 
    "\tThis script is written for python 2.7.11\n" + 
    "\tI haven't written the usage tutorial yet.  Oops.  Do this now please."
    )      
    
    
# Read Commandline Arguments.  Return true if everything looks okay for read extraction.
def readArgs():
    # Default to None.  So I can easily check if they were not passed in.
   
    global inputReadFileName
    global outputResultDirectory
    global numberIterations
    global consensusFileName
    global numberThreads
    
    inputReadFileName        = None
    outputResultDirectory    = None
    consensusFileName        = None
    numberIterations         = 1
    numberThreads            = 1

    if(len(sys.argv) < 3):
        print ('I don\'t think you have enough arguments.\n')
        usage()
        return False    

    # https://www.tutorialspoint.com/python/python_command_line_arguments.htm
    try:
        opts, args = getopt.getopt(sys.argv[1:]
            ,"hvi:o:r:c:t:"
            ,[ "help", "version", "iterations=","outputdir=","reads=",'consensus=','threads='])

        for opt, arg in opts:

            if opt in ('-h', '--help'):
                print (SoftwareVersion)
                usage()
                return False

            elif opt in ('-v', '--version'):
                print (SoftwareVersion)
                return False

            elif opt in ("-i", "--iterations"):
                numberIterations = arg
            elif opt in ("-o", "--outputdir"):
                outputResultDirectory = arg
            elif opt in ("-r", "--reads"):
                inputReadFileName = arg
            elif opt in ("-c", "--consensus"):
                consensusFileName = arg
            elif opt in ("-c", "--threads"):
                numberThreads = arg
            else:
                print('Unknown Commandline Option:' + str(opt) + ':' + str(arg))
                raise Exception('Unknown Commandline Option:' + str(opt) + ':' + str(arg))
            

    except getopt.GetoptError, errorMessage:
        print ('Something seems wrong with your commandline parameters.')
        print (errorMessage)
        usage()
        return False

    # Consensus,threads is optional, the rest are necessary.
    #print('Reads:' + inputReadFileName)
    #print('Number Iterations:' + str(numberIterations))
    #print('Output Directory:' + outputResultDirectory)
    #print('Consensus Filename:' + str(consensusFileName))
    #print('Threads:' + str(numberThreads))
    
    #TODO: Iterations should be > 0

    return True

if __name__=='__main__':

    try:    
        if(readArgs()):
            print('Commandline arguments look fine.\nThe hour is at hand. Let us wrangle the Alleles.')
            
            myAlleleWrangler = AlleleWrangler(inputReadFileName, outputResultDirectory, consensusFileName, numberIterations, numberThreads)
            myAlleleWrangler.wrangle()
            
            print ('I am done wrangling alleles for now, have a nice day.')    
        else:
            print('\nI\'m giving up because I was not satisfied with your commandline arguments.')  
            
    except Exception:
        # Top Level exception handling like a pro.
        # This is not really doing anything.
        print 'Fatal problem during read extraction:'
        print sys.exc_info()
        raise

