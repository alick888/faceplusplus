from facepplib import FacePP

facepp = FacePP(api_key='CD6RZlJuI8PostJBrrnkvGngb-gnSJbs',
                 api_secret='lHp0GrPsZvxMHdgYUtEiAExZ_JFPKia4')
url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
image_url = 'https://www.faceplusplus.com/scripts/demoScript/images/demo-pic6.jpg'
image = facepp.image.get(image_url=image_url,
                         return_attributes=['smiling', 'age'])
print(image.image_id)
