'''
Spectrology
This script is able to encode an image into audio file whose spectrogram represents input image.

License: MIT
Website: https://github.com/solusipse/spectrology
'''

from PIL import Image
import wave, math, array, argparse, sys, timeit

def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("INPUT", help="Name of the image to be convected.")
    parser.add_argument("-o", "--output", help="Name of the output wav file. Default value: out.wav).")
    parser.add_argument("-b", "--bottom", help="Bottom frequency range. Default value: 200.", type=int)
    parser.add_argument("-t", "--top", help="Top frequency range. Default value: 20000.", type=int)
    parser.add_argument("-p", "--pixels", help="Pixels per second. Default value: 30.", type=int)
    parser.add_argument("-s", "--sampling", help="Sampling rate. Default value: 44100.", type=int)
    args = parser.parse_args()

    minfreq = 200
    maxfreq = 20000
    wavrate = 44100
    pxs     = 30
    output  = "out.wav"

    if args.output:
        output = args.output
    if args.bottom:
        minfreq = args.bottom
    if args.top:
        maxfreq = args.top
    if args.pixels:
        pxs = args.pixels
    if args.sampling:
        wavrate = args.sampling

    print('Input file: %s.' % args.INPUT)
    print('Frequency range: %d - %d.' % (minfreq, maxfreq))
    print('Pixels per second: %d.' % pxs)
    print('Sampling rate: %d.' % wavrate)

    return (args.INPUT, output, minfreq, maxfreq, pxs, wavrate)

def convert(inpt, output, minfreq, maxfreq, pxs, wavrate):
    img = Image.open(inpt).convert('RGB')

    output = wave.open(output, 'w')
    output.setparams((1, 2, wavrate, 0, 'NONE', 'not compressed'))

    freqrange = maxfreq - minfreq
    interval = freqrange / img.size[1]

    fpx = wavrate / pxs
    data = array.array('h')

    tm = timeit.default_timer()

    for x in range(img.size[0]):
        row = []
        pos = 0
        for y in range(img.size[1]):
            yinv = img.size[1] - y - 1
            amp = color( img.getpixel((x,y)) )
            if (amp > 0):
                row.append( genwave(yinv * interval + minfreq, amp, fpx, wavrate) )

        for i in range(fpx):
            for j in row:
                try:
                    data[i + x * fpx] += j[i]
                except:
                    data.insert(i + x * fpx, j[i])

        sys.stdout.write("Conversion progress: %d%%   \r" % (float(x) / img.size[0]*100) )
        sys.stdout.flush()

    output.writeframes(data.tostring())
    output.close()

    tms = timeit.default_timer()

    print("Conversion progress: 100%")
    print("Success. Completed in %d seconds." % int(tms-tm))

def color(rgb):
    return (rgb[0] + rgb[1] + rgb[2])/3

def genwave(frequency, amplitude, samples, samplerate):
    cycles = samples * frequency / samplerate
    audioArray = []
    for i in range(samples):
        x = math.sin(float(cycles) * 2 * math.pi * i / float(samples)) * float(amplitude)
        audioArray.append(int(math.floor(x)))
    return audioArray

if __name__ == '__main__':
    inpt = parser()
    convert(*inpt)
