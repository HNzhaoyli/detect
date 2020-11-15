import cv2
import os

def  Cropimg(imgpath,savepath):
    pathDir = os.listdir(imgpath)
    for path in pathDir:
        imgplace = os.path.join(imgpath,path)
        save = os.path.join(savepath,path)
        #print(save)
        if not os.path.isdir(save):
            os.mkdir(save)
        img = cv2.imread(imgplace)
        sp = img.shape
        #print(img.shape)
        a = int(sp[0]-sp[0])
        b = int(sp[0]/3-10)
        c = int(sp[0]/2+20)
        d = int(sp[0]-5)
        head_img = img[a:b, a:sp[1]]
        body_img = img[b:c , a:sp[1]]
        leg_img = img[c:d , a:sp[1]]


        cv2.imwrite(os.path.join(save,'head_img'+'.jpg'),head_img)
        cv2.imwrite(os.path.join(save,'body_img'+'.jpg'),body_img)
        cv2.imwrite(os.path.join(save,'leg_img'+'.jpg'),leg_img)

if __name__ == '__main__':
    imgpath = r'F:\image\img'
    savepath = r'F:\image\img4'
    Cropimg(imgpath,savepath)
    print('Finished .... ')


