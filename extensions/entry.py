import os
from pyraabe_3199c8b import pyraabe

def main(infile, outdir, vector, extruded):
    """
    Modified GUI response interface for PyRaabe functionality. Does not use command line args

    """
    infiles = [infile]
    if (not outdir):
        outdir = os.path.dirname(infiles[0])
    gravity_vector = vector
    extruded = extruded

    # iterate inputs
    centerline_paths = []
    raabe_paths = []
    for infile in infiles:
        # outputs
        basename = os.path.splitext(os.path.basename(infile))[0]
        centerline_path = os.path.join(outdir, basename + '_centerline.vtp')
        centerline_paths.append(centerline_path)
        raabe_path = os.path.join(outdir, basename + '_raabe.csv')
        raabe_paths.append(raabe_path)
        coord_path = os.path.join(outdir, basename + '_coordinates.csv')

        # centerline extraction
        if not os.path.exists(centerline_path):
            pyraabe.centerline.compute(infile, centerline_path)
        else:
            print('{} already exists.\n Skipping centerline calculation.'.format(centerline_path))

    # merge
    if len(centerline_paths) > 1:
        raabe, raabe_all = pyraabe.table.merge(centerline_paths[0],
                                               centerline_paths[1:],
                                               gravity_vector,
                                               extruded)

        # save individual raabes
        for i in range(len(raabe_paths)):
            raabe_all[i].drop(columns='endpoint_idx').to_csv(raabe_paths[i], sep=',')

        # save merged raabe
        raabe.drop(columns='endpoint_idx').to_csv(os.path.join(outdir, 'merged_raabe.csv'), sep=',')

    # single
    else:
        # read in centerline
        centerline = pyraabe.centerline.read(centerline_path)

        # save coordinates
        pyraabe.centerline.to_dataframe(centerline).to_csv(coord_path)

        # raabe generation
        raabe = pyraabe.table.generate(centerline, gravity_vector, extruded)

        # drop column and save
        raabe.drop(columns='endpoint_idx').to_csv(raabe_path, sep=',')
    
    print('\n Complete: ', infile)