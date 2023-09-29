from PIL import Image
import numpy

def check_hash():
    image = numpy.asarray(Image.open('IMG.png'))
    submission = numpy.asarray(Image.open('IMG2.png'))
    if image.shape != submission.shape:
        print("image.shape != submission.shape")
        return False
    same = numpy.bitwise_xor(image, submission)

    if (numpy.sum(same) == 0):
        print("same")
        return False
    im_alt = numpy.fft.fftn(image)
    in_alt = numpy.fft.fftn(submission)
    im_hash = numpy.std(im_alt)
    in_hash = numpy.std(in_alt)
    print("im_hash: ", im_hash)
    print("in_hash: ", in_hash)
    if im_hash - in_hash < 1 and im_hash - in_hash > -1:
        print("im_hash: ", im_hash)

        return True


    print("Hashes are different")
    return False

if __name__ == '__main__':
    print(check_hash())
