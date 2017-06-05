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

# Version 1.0 

# See the file README.MD for how to set up your anaconda environment.

# You should change the following input variables before you run this program:
# The $Rundate variable is included in the name of the output files, 
# You can fill that variable with whatever text you wish to appear there
# Don't use special characters ("*", "/", "\", "$", "?", etc.)

ReadInputFile="/home/eggs/Workspace/Github/allele-wrangler/data/EvenSmallerReads.fasta"
#ReadInputFile="/home/eggs/Workspace/Github/allele-wrangler/data/ToyReads.fasta"
#ReadInputFile="/home/eggs/Workspace/Data/SampleReads_extracts/SampleReads_BC01_TwoDir_reads.fasta"
ResultsOutputDirectory="/home/eggs/Workspace/wrangled_results_toy"
NumberIterations="5"
ThreadCount="4"

source activate minionvironment

cd src

python AlleleWrangler_Main.py \
 --reads=$ReadInputFile \
 --outputdir=$ResultsOutputDirectory \
 --iterations=$NumberIterations \
 --threads=$ThreadCount

source deactivate
