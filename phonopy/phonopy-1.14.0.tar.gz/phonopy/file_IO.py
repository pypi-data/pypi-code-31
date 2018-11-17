# Copyright (C) 2011 Atsushi Togo
# All rights reserved.
#
# This file is part of phonopy.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in
#   the documentation and/or other materials provided with the
#   distribution.
#
# * Neither the name of the phonopy project nor the names of its
#   contributors may be used to endorse or promote products derived
#   from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import sys
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import numpy as np


#
# FORCE_SETS
#
def write_FORCE_SETS(dataset, filename='FORCE_SETS'):
    num_atom = dataset['natom']
    displacements = dataset['first_atoms']
    forces = [x['forces'] for x in dataset['first_atoms']]

    # Write FORCE_SETS
    with open(filename, 'w') as fp:
        fp.write("%-5d\n" % num_atom)
        fp.write("%-5d\n" % len(displacements))
        for count, disp in enumerate(displacements):
            fp.write("\n%-5d\n" % (disp['number'] + 1))
            fp.write("%20.16f %20.16f %20.16f\n" %
                     (tuple(disp['displacement'])))

            for f in forces[count]:
                fp.write("%15.10f %15.10f %15.10f\n" % (tuple(f)))


def parse_FORCE_SETS(natom=None,
                     is_translational_invariance=False,
                     filename="FORCE_SETS"):
    with open(filename, 'r') as f:
        return _get_set_of_forces(
            f,
            natom=natom,
            is_translational_invariance=is_translational_invariance)


def parse_FORCE_SETS_from_strings(strings,
                                  natom=None,
                                  is_translational_invariance=False):
    return _get_set_of_forces(
        StringIO(strings),
        natom=natom,
        is_translational_invariance=is_translational_invariance)


def _get_set_of_forces(f, natom=None, is_translational_invariance=False):
    first_line_ary = _get_line_ignore_blank(f).split()
    f.seek(0)
    if len(first_line_ary) == 1:
        if natom is None or int(first_line_ary[0]) == natom:
            return _get_set_of_forces_type1(f, is_translational_invariance)
        else:
            msg = "Number of forces is not consistent with supercell setting."
            raise RuntimeError(msg)
    elif len(first_line_ary) == 6:
        return _get_set_of_forces_type2(f, natom)


def _get_set_of_forces_type2(f, natom):
    data = np.loadtxt(f, dtype='double')
    if data.shape[1] != 6 or data.shape[0] % natom != 0:
        msg = "Data shape of forces and displacements is incorrect."
        raise RuntimeError(msg)
    data = data.reshape(-1, natom, 6)
    dataset = {'natom': natom}
    dataset['displacements'] = np.array(data[:, :, :3],
                                        dtype='double', order='C')
    dataset['forces'] = np.array(data[:, :, 3:], dtype='double', order='C')
    return dataset


def _get_set_of_forces_type1(f, is_translational_invariance):
    set_of_forces = []
    num_atom = int(_get_line_ignore_blank(f))
    num_displacements = int(_get_line_ignore_blank(f))

    for i in range(num_displacements):
        line = _get_line_ignore_blank(f)
        atom_number = int(line)
        line = _get_line_ignore_blank(f).split()
        displacement = np.array([float(x) for x in line])
        forces_tmp = []
        for j in range(num_atom):
            line = _get_line_ignore_blank(f).split()
            forces_tmp.append(np.array([float(x) for x in line]))
        forces_tmp = np.array(forces_tmp, dtype='double')

        if is_translational_invariance:
            forces_tmp -= np.sum(forces_tmp, axis=0) / len(forces_tmp)

        forces = {'number': atom_number - 1,
                  'displacement': displacement,
                  'forces': forces_tmp}
        set_of_forces.append(forces)

    dataset = {'natom': num_atom,
               'first_atoms': set_of_forces}

    return dataset


def _get_line_ignore_blank(f):
    line = f.readline().strip()
    if line == '':
        line = _get_line_ignore_blank(f)
    return line


def collect_forces(f, num_atom, hook, force_pos, word=None):
    for line in f:
        if hook in line:
            break

    forces = []
    for line in f:
        if line.strip() == '':
            continue
        if word is not None:
            if word not in line:
                continue

        elems = line.split()
        if len(elems) > force_pos[2]:
            try:
                forces.append([float(elems[i]) for i in force_pos])
            except ValueError:
                forces = []
                break
        else:
            return False

        if len(forces) == num_atom:
            break

    return forces


def iter_collect_forces(filename,
                        num_atom,
                        hook,
                        force_pos,
                        word=None,
                        max_iter=1000):
    with open(filename) as f:
        forces = []
        prev_forces = []

        for i in range(max_iter):
            forces = collect_forces(f, num_atom, hook, force_pos, word=word)
            if not forces:
                forces = prev_forces[:]
                break
            else:
                prev_forces = forces[:]

        if i == max_iter - 1:
            sys.stderr.write("Reached to max number of iterations (%d).\n" %
                             max_iter)

        return forces


#
# FORCE_CONSTANTS, force_constants.hdf5
#
def write_FORCE_CONSTANTS(force_constants,
                          filename='FORCE_CONSTANTS',
                          p2s_map=None):
    """Write force constants in text file format.

    Parameters
    ----------
    force_constants: ndarray
        Force constants
        shape=(n_satom,n_satom,3,3) or (n_patom,n_satom,3,3)
        dtype=double
    filename: str
        Filename to be saved
    p2s_map: ndarray
        Primitive atom indices in supercell index system
        dtype=intc

    """

    if p2s_map is not None and len(p2s_map) == force_constants.shape[0]:
        indices = p2s_map
    else:
        indices = np.arange(force_constants.shape[0], dtype='intc')

    with open(filename, 'w') as w:
        fc_shape = force_constants.shape
        w.write("%4d %4d\n" % fc_shape[:2])
        for i, s_i in enumerate(indices):
            for j in range(fc_shape[1]):
                w.write("%d %d\n" % (s_i + 1, j + 1))
                for vec in force_constants[i][j]:
                    w.write(("%22.15f"*3 + "\n") % tuple(vec))


def write_force_constants_to_hdf5(force_constants,
                                  filename='force_constants.hdf5',
                                  p2s_map=None):
    """Write force constants in hdf5 format.

    Parameters
    ----------
    force_constants: ndarray
        Force constants
        shape=(n_satom,n_satom,3,3) or (n_patom,n_satom,3,3)
        dtype=double
    filename: str
        Filename to be saved
    p2s_map: ndarray
        Primitive atom indices in supercell index system
        shape=(n_patom,)
        dtype=intc

    """

    try:
        import h5py
    except ImportError:
        raise ModuleNotFoundError("You need to install python-h5py.")

    with h5py.File(filename, 'w') as w:
        w.create_dataset('force_constants', data=force_constants)
        if p2s_map is not None:
            w.create_dataset('p2s_map', data=p2s_map)


def parse_FORCE_CONSTANTS(filename="FORCE_CONSTANTS",
                          p2s_map=None):
    with open(filename) as fcfile:
        idx1 = []

        line = fcfile.readline()
        idx = [int(x) for x in line.split()]
        if len(idx) == 1:
            idx = [idx[0], idx[0]]
        force_constants = np.zeros((idx[0], idx[1], 3, 3), dtype='double')
        for i in range(idx[0]):
            for j in range(idx[1]):
                s_i = int(fcfile.readline().split()[0]) - 1
                if s_i not in idx1:
                    idx1.append(s_i)
                tensor = []
                for k in range(3):
                    tensor.append([float(x)
                                   for x in fcfile.readline().split()])
                force_constants[i, j] = tensor

        check_force_constants_indices(idx, idx1, p2s_map, filename)

        return force_constants


def read_force_constants_hdf5(filename="force_constants.hdf5",
                              p2s_map=None):
    try:
        import h5py
    except ImportError:
        raise ModuleNotFoundError("You need to install python-h5py.")

    with h5py.File(filename, 'r') as f:
        if 'fc2' in f:
            key = 'fc2'
        elif 'force_constants' in f:
            key = 'force_constants'
        else:
            raise RuntimeError("%s doesn't contain necessary information" %
                               filename)

        fc = f[key][:]
        if 'p2s_map' in f:
            p2s_map_in_file = f['p2s_map'][:]
            check_force_constants_indices(fc.shape[:2],
                                          p2s_map_in_file,
                                          p2s_map,
                                          filename)
        return fc


def check_force_constants_indices(shape, indices, p2s_map, filename):
    if shape[0] != shape[1] and p2s_map is not None:
        if len(p2s_map) != len(indices) or (p2s_map != indices).any():
            text = ("%s file is inconsistent with the calculation setting. "
                    "PRIMITIVE_AXIS may not be set correctly.") % filename
            raise RuntimeError(text)


#
# disp.yaml
#
def parse_disp_yaml(filename="disp.yaml", return_cell=False):
    try:
        import yaml
    except ImportError:
        raise ModuleNotFoundError("You need to install python-yaml.")

    try:
        from yaml import CLoader as Loader
    except ImportError:
        from yaml import Loader

    with open(filename) as f:
        dataset = yaml.load(f, Loader=Loader)
        natom = dataset['natom']
        new_dataset = {}
        new_dataset['natom'] = natom
        new_first_atoms = []
        for first_atoms in dataset['displacements']:
            first_atoms['atom'] -= 1
            atom1 = first_atoms['atom']
            disp1 = first_atoms['displacement']
            new_first_atoms.append({'number': atom1,
                                    'displacement': disp1})
        new_dataset['first_atoms'] = new_first_atoms

        if return_cell:
            cell = get_cell_from_disp_yaml(dataset)
            return new_dataset, cell
        else:
            return new_dataset


def write_disp_yaml_from_dataset(dataset, supercell, filename='disp.yaml'):
    displacements = [(d['number'],) + tuple(d['displacement'])
                     for d in dataset['first_atoms']]
    write_disp_yaml(displacements, supercell, filename=filename)


def write_disp_yaml(displacements,
                    supercell,
                    filename='disp.yaml'):
    text = []
    text.append("natom: %4d" % supercell.get_number_of_atoms())
    text.append("displacements:")
    for i, disp in enumerate(displacements):
        text.append("- atom: %4d" % (disp[0] + 1))
        text.append("  displacement:")
        text.append("    [ %20.16f,%20.16f,%20.16f ]" % tuple(disp[1:4]))

    text.append(str(supercell))

    with open(filename, 'w') as w:
        w.write("\n".join(text))


#
# DISP (old phonopy displacement format)
#
def parse_DISP(filename='DISP'):
    with open(filename) as disp:
        displacements = []
        for line in disp:
            if line.strip() != '':
                a = line.split()
                displacements.append(
                    [int(a[0])-1, float(a[1]), float(a[2]), float(a[3])])
        return displacements


#
# Parse supercell in disp.yaml
#
def get_cell_from_disp_yaml(dataset):
    from phonopy.structure.atoms import PhonopyAtoms

    lattice = dataset['lattice']
    if 'points' in dataset:
        data_key = 'points'
        pos_key = 'coordinates'
    elif 'atoms' in dataset:
        data_key = 'atoms'
        pos_key = 'position'
    else:
        data_key = None
        pos_key = None

    positions = [x[pos_key] for x in dataset[data_key]]
    symbols = [x['symbol'] for x in dataset[data_key]]
    cell = PhonopyAtoms(cell=lattice,
                        scaled_positions=positions,
                        symbols=symbols,
                        pbc=True)
    return cell


#
# QPOINTS
#
def parse_QPOINTS(filename="QPOINTS"):
    from phonopy.cui.settings import fracval

    with open(filename, 'r') as f:
        num_qpoints = int(f.readline().strip())
        qpoints = []
        for i in range(num_qpoints):
            qpoints.append([fracval(x) for x in f.readline().strip().split()])
        return np.array(qpoints)


#
# BORN
#
def parse_BORN(primitive, symprec=1e-5, is_symmetry=True, filename="BORN"):
    with open(filename, 'r') as f:
        return _parse_BORN_from_file_object(f, primitive, symprec, is_symmetry)


def parse_BORN_from_strings(strings, primitive,
                            symprec=1e-5, is_symmetry=True):
    f = StringIO(strings)
    return _parse_BORN_from_file_object(f, primitive, symprec, is_symmetry)


def _parse_BORN_from_file_object(f, primitive, symprec, is_symmetry):
    from phonopy.structure.symmetry import Symmetry
    symmetry = Symmetry(primitive, symprec=symprec, is_symmetry=is_symmetry)
    return get_born_parameters(f, primitive, symmetry)


def get_born_parameters(f, primitive, prim_symmetry):
    line_arr = f.readline().split()
    if len(line_arr) < 1:
        print("BORN file format of line 1 is incorrect")
        return False

    factor = None
    G_cutoff = None
    Lambda = None

    if len(line_arr) > 0:
        try:
            factor = float(line_arr[0])
        except (ValueError, TypeError):
            factor = None
    if len(line_arr) > 1:
        try:
            G_cutoff = float(line_arr[1])
        except (ValueError, TypeError):
            G_cutoff = None
    if len(line_arr) > 2:
        try:
            Lambda = float(line_arr[2])
        except (ValueError, TypeError):
            Lambda = None

    # Read dielectric constant
    line = f.readline().split()
    if not len(line) == 9:
        print("BORN file format of line 2 is incorrect")
        return False
    dielectric = np.reshape([float(x) for x in line], (3, 3))

    # Read Born effective charge
    independent_atoms = prim_symmetry.get_independent_atoms()
    borns = np.zeros((primitive.get_number_of_atoms(), 3, 3),
                     dtype='double', order='C')

    for i in independent_atoms:
        line = f.readline().split()
        if len(line) == 0:
            print("Number of lines for Born effect charge is not enough.")
            return False
        if not len(line) == 9:
            print("BORN file format of line %d is incorrect" % (i + 3))
            return False
        borns[i] = np.reshape([float(x) for x in line], (3, 3))

    # Check that the number of atoms in the BORN file was correct
    line = f.readline().split()
    if len(line) > 0:
        print("Too many atoms in the BORN file (it should only contain "
              "symmetry-independent atoms)")
        return False

    _expand_borns(borns, primitive, prim_symmetry)
    non_anal = {'born': borns,
                'factor': factor,
                'dielectric': dielectric}
    if G_cutoff is not None:
        non_anal['G_cutoff'] = G_cutoff
    if Lambda is not None:
        non_anal['Lambda'] = Lambda

    return non_anal


def _expand_borns(borns, primitive, prim_symmetry):
    from phonopy.harmonic.force_constants import similarity_transformation

    # Expand Born effective charges to all atoms in the primitive cell
    rotations = prim_symmetry.get_symmetry_operations()['rotations']
    map_operations = prim_symmetry.get_map_operations()
    map_atoms = prim_symmetry.get_map_atoms()

    for i in range(primitive.get_number_of_atoms()):
        # R_cart = L R L^-1
        rot_cartesian = similarity_transformation(
            primitive.get_cell().transpose(), rotations[map_operations[i]])
        # R_cart^T B R_cart^-T (inverse rotation is required to transform)
        borns[i] = similarity_transformation(rot_cartesian.transpose(),
                                             borns[map_atoms[i]])


#
# e-v.dat, thermal_properties.yaml
#
def read_thermal_properties_yaml(filenames):
    import yaml
    try:
        from yaml import CLoader as Loader
    except ImportError:
        from yaml import Loader

    thermal_properties = []
    num_modes = []
    num_integrated_modes = []
    for filename in filenames:
        with open(filename) as f:
            tp_yaml = yaml.load(f, Loader=Loader)
            thermal_properties.append(tp_yaml['thermal_properties'])
            if 'num_modes' in tp_yaml and 'num_integrated_modes' in tp_yaml:
                num_modes.append(tp_yaml['num_modes'])
                num_integrated_modes.append(tp_yaml['num_integrated_modes'])

    temperatures = [v['temperature'] for v in thermal_properties[0]]
    temp = []
    cv = []
    entropy = []
    fe_phonon = []
    for i, tp in enumerate(thermal_properties):
        temp.append([v['temperature'] for v in tp])
        if not np.allclose(temperatures, temp):
            msg = ['', ]
            msg.append("Check your input files")
            msg.append("Disagreement of temperature range or step")
            for t, fname in zip(temp, filenames):
                msg.append("%s: Range [ %d, %d ], Step %f" %
                           (fname, int(t[0]), int(t[-1]), t[1] - t[0]))
            msg.append('')
            msg.append("Stop phonopy-qha")
            raise RuntimeError(msg)
        cv.append([v['heat_capacity'] for v in tp])
        entropy.append([v['entropy'] for v in tp])
        fe_phonon.append([v['free_energy'] for v in tp])

    # shape=(temperatures, volumes)
    cv = np.array(cv).T
    entropy = np.array(entropy).T
    fe_phonon = np.array(fe_phonon).T

    return (temperatures, cv, entropy, fe_phonon, num_modes,
            num_integrated_modes)


def read_v_e(filename):
    data = _parse_QHA_data(filename)
    if data.shape[1] != 2:
        msg = ("File format of %s is incorrect for reading e-v data." %
               filename)
        raise RuntimeError(msg)
    volumes, electronic_energies = data.T
    return volumes, electronic_energies


def read_efe(filename):
    data = _parse_QHA_data(filename)
    temperatures = data[:, 0]
    free_energies = data[:, 1:]
    return temperatures, free_energies


def _parse_QHA_data(filename):
    data = []
    with open(filename) as f:
        for line in f:
            if line.strip() == '' or line.strip()[0] == '#':
                continue
            if '#' in line:
                data.append([float(x) for x in line.split('#')[0].split()])
            else:
                data.append([float(x) for x in line.split()])
        return np.array(data)
