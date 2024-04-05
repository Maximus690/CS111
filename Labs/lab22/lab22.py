import matplotlib.pyplot as plt


def get_gpa_sat(filename):
    gpa = []
    sat = []
    with open(filename, 'r') as input_file:
        input_file.readline()
        for line in input_file:
            line = line.split(',')
            gpa.append(float(line[2]))
            sat.append(float(line[1]))
    return gpa, sat


def read_spectra(filename):
    wavelength = []
    flux = []
    with open(filename, 'r') as input_file:
        input_file.readline()
        for line in input_file:
            w, f = map(float, line.split())
            wavelength.append(w)
            flux.append(f)
    return wavelength, flux


def plot_histogram():
    # Write Q1 code here
    gpa, sat = get_gpa_sat('admission_algorithms_dataset.csv')
    plt.hist(gpa)
    plt.savefig('gpa.png')
    plt.clf()

    plt.hist(sat)
    plt.savefig('sat_score.png')
    plt.clf()


def plot_scatter():
    # Write Q2 code here
    gpa, sat = get_gpa_sat('admission_algorithms_dataset.csv')
    plt.scatter(gpa, sat)
    plt.savefig('correlation.png')
    plt.clf()


def plot_spectra():
    # Write Q3 code here
    wavelength, flux = read_spectra('spectra.txt')
    wavelength2, flux2 = read_spectra('spectrum2.txt')
    plt.plot(wavelength, flux, 'b')
    plt.plot(wavelength2, flux2, 'g')
    plt.savefig('spectra.png')
    plt.clf()


def main():
    plot_histogram()
    plot_scatter()
    plot_spectra()



if __name__ == "__main__":
    main()
