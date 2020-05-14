import torch
import argparse

parser = argparse.ArgumentParser(description = 'Grid Cell visualization Using GTMSM')

# batch size
parser.add_argument('--batch-size', type = int, default = 4, metavar = 'N', help = 'batch size for training (default : 4)')

# number of epochs
parser.add_argument('--epochs', type=int, default = 50, metavar = 'N', help = 'number of epochs for training (default : 50)')

# cuda training
parser.add_argument('--no-cuda', action = 'store_true', default = False, help = 'enable cuda training')

# seed
parser.add_argument('--seed', type = int, default = 7,  metavar = 'S', help = 'random seed (default : 7)')

# saving interval 
parser.add_argument('--save-interval', type = int, default = 1 , metavar = 'N', help = 'number of epochs between consecutive saves of the model (default : 1)')

# log interval
parser.add_argument('--log-interval', type = int, default = 10, help = "number of batches to train before logging training status (default : 10)")

# gradient clip
# i am not sure what this does (lets see)
parser.add_argument('--gradient-clip', type = int, default = 10 , metavar = 'N', help = "maximum norm of gradient to be used (default : 10)")

args = parser.parse_args()
args.cuda = not args.no_cuda and torch.cuda.is_available()

if args.cuda :

	torch.cuda.manual_seed_all(args.seed)
	
device = torch.device("cuda" if args.cuda else "cpu")

kwargs = {'num_workeres' : 1, 'pin_memory' : True} if args.cuda else {}

#print("we are cool here")