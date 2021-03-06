#!/usr/bin/env python

__author__ = '{{cookiecutter.author_email}}'


from d3r.celppade.customdock import Dock

class {{cookiecutter.dock_classname}}(Dock):
    """Abstract class defining methods for a custom docking solution
    for CELPP
    """


    def lig_technical_prep(self, sci_prepped_lig):
        """Technical preparation" is the step immediate preceding
        docking. During this step, you should perform any file
        conversions or processing that are specific to your docking
        program.
        :param sci_prepped_lig: Scientifically prepared ligand file
        :returns: This implementation merely returns the value of
        `sci_prepped_lig` in a list
        """
        return super({{cookiecutter.dock_classname}},
                     self).lig_technical_prep(sci_prepped_lig)

    def receptor_technical_prep(self, sci_prepped_receptor, pocket_center):
        """Technical preparation" is the step immediately preceding
        docking. During this step, you should perform any file
        conversions or processing that are specific to your docking
        program.
        """

        # Finally, we return the filenames that will be needed in the
        # docking step. This list is passed to the dock() function as the
        # tech_prepped_receptor_list argument. Here we pass the docking
        # box file (for the docking) and the original scientifically
        # prepped ligand pdb, as that's the easiest way to return the
        # final receptor conformation.
        return super({{cookiecutter.dock_classname}},
                     self).receptor_technical_prep(sci_prepped_receptor, pocket_center)

    def dock(self, tech_prepped_lig_list, tech_prepped_receptor_list, output_receptor_pdb, output_lig_mol):
        """# The dock step needs to run the actual docking algorithm. Its first two
        # arguments are the return values from the technical preparation
        # functions for the ligand and receptor. The outputs from this
        # step must be two files - a pdb with the filename specified in
        # the output_receptor_pdb argument, and a mol with the filename
        # specified in the output_ligand_mol argument.
        :returns: Always returns False
        """
        return super({{cookiecutter.dock_classname}},
                     self).dock(tech_prepped_lig_list,
                                tech_prepped_receptor_list,
                                output_receptor_pdb, output_lig_mol)


if ("__main__") == (__name__):
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("-s", "--sciprepdir", metavar="PATH", help = "PATH where we can find the scientific protein and lig prep output")
    parser.add_argument("-o", "--outdir", metavar = "PATH", help = "PATH where we will put the docking output")
    parser.add_argument("-u", "--update", action = "store_true",  help = "Update the docking result", default = False)
    logger = logging.getLogger()
    logging.basicConfig( format  = '%(asctime)s: %(message)s', datefmt = '%m/%d/%y %I:%M:%S', filename = 'final.log', filemode = 'w', level   = logging.INFO )
    opt = parser.parse_args()
    sci_prep_dir = opt.sciprepdir
    dock_dir = opt.outdir
    update = opt.update
    #running under this dir
    abs_running_dir = os.getcwd()
    log_file_path = os.path.join(abs_running_dir, 'final.log')
    log_file_dest = os.path.join(os.path.abspath(dock_dir), 'final.log')
    docker = {{cookiecutter.dock_classname}}()
    docker.run_dock(sci_prep_dir, dock_dir, update = update)
    #move the final log file to the result dir
    commands.getoutput("mv %s %s"%(log_file_path, log_file_dest))
