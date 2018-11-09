#!/usr/local/bin/env python

from .fluorify import Scanning
from docopt import docopt

# =============================================================================================
# COMMAND-LINE INTERFACE
# =============================================================================================

usage = """
FLUORIFY
Usage:
  Fluorify [--output_folder=STRING] [--mol_file=STRING] [--ligand_name=STRING] [--complex_name=STRING] 
           [--solvent_name=STRING] [--atom_list=LIST] [--num_frames=INT] [--net_charge=INT] [--job_type=STRING]...
"""


def main(argv=None):
    args = docopt(usage, argv=argv, options_first=True)

    msg = 'No {0} specified using default {1}'

    if args['--mol_file']:
        mol_file = args['--mol_file']
    else:
        mol_file = 'ligand'
        print(msg.format('mol file', mol_file + '.mol2'))

    if args['--ligand_name']:
        ligand_name = args['--ligand_name']
    else:
        ligand_name ='MOL'
        print(msg.format('ligand residue name', ligand_name))

    if args['--complex_name']:
        complex_name = args['--complex_name']
    else:
        complex_name = 'complex'
        print(msg.format('complex name', complex_name))

    if args['--solvent_name']:
        solvent_name = args['--solvent_name']
    else:
        solvent_name = 'solvent'
        print(msg.format('solvent name', solvent_name))

    if args['--atom_list']:
        atom_list = []
        pairs = args['--atom_list']
        pairs = pairs.replace(" ", "")
        pairs = pairs.split('and')
        for pair in pairs:
            tmp = []
            pair = pair.split(',')
            for atom in pair:
                tmp.append(atom)
            atom_list.append(tmp)
    else:
        atom_list = []

    if args['--job_type']:
        job_type = args['--job_type'][0]
        job_name = args['--job_type'][0]
        allowed_elements = ['F', 'Cl']
        allowed_carbon_types = ['1', '2', '3', 'ar']
        job_type = job_type.split('_')
        if job_type[0] not in allowed_elements:
            raise ValueError('Allowed elements {}'.format(allowed_elements))
        elif job_type[1] not in allowed_carbon_types:
            raise ValueError('Allowed carbon types {}'.format(allowed_carbon_types))
        else:
                pass
    else:
        job_type = ['F', 'ar']
        job_name = 'F_ar'
        print(msg.format('job_type', job_type))

    if args['--output_folder']:
        output_folder = args['--output_folder']
    else:
        output_folder = './' + mol_file + '_' + job_name + '/'
        print(msg.format('output folder', output_folder))

    if args['--num_frames']:
        num_frames = int(args['--num_frames'])
    else:
        num_frames = 9500
        print(msg.format('number of frames', num_frames))

    if args['--net_charge']:
        net_charge = int(args['--net_charge'])
    else:
        net_charge = None
        print(msg.format('net charge', net_charge))

    Scanning(output_folder, mol_file, ligand_name, net_charge,
             complex_name, solvent_name, job_type, atom_list, num_frames)
