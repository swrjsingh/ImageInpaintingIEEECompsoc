# Image Inpainting using Generative Adverserial Networks
### Abstract
This project was done as a semester-long project under IEEE CompSoc Envision 2024

Run the following commands to run the app locally
```
git clone https://github.com/swrjsingh/ImageInpaintingIEEECompsoc.git
cd ImageInpaintingIEEECompsoc
pip install -r requirements.txt
python app.py
```

## Introduction

Image inpainting is a computer vision task involving filling in missing or damaged parts of an image, with applications in photo editing, image restoration, and object removal. This project focuses on using PatchGAN, a type of Generative Adversarial Network (GAN), for image inpainting on the CelebA dataset, which contains over 200,000 celebrity images.

## Methodology

### Dataset Preparation
- The CelebA dataset comprises images with various resolutions and annotations like facial keypoints and attributes.
- Preprocessing involves extracting images and masks indicating regions to be inpainted.

### Model Architecture
- PatchGAN is employed, tailored for image-to-image translation tasks.
- The PatchGAN Discriminator classifies image patches as real or fake, ensuring high-quality, coherent outputs.

### Training
- The model is trained using adversarial and reconstruction losses.
- Adversarial loss drives the generator to produce realistic inpainted images, while reconstruction loss ensures inpainted regions match the surrounding context.

### Results
- The trained model effectively inpaints missing regions in the CelebA dataset.
- Qualitative evaluation reveals visually pleasing results with realistic textures and coherent structures.

### Flask Website

#### Frontend
- Users can upload images and crop portions.
- They can specify areas to inpaint or let the model detect and inpaint missing regions.

#### Backend
- The backend integrates the trained PatchGAN model for inpainting.
- Upon receiving an image, the backend processes it through the model and returns the inpainted result.

## Conclusion

This project showcases PatchGAN's effectiveness for image inpainting on the CelebA dataset. The Flask website provides a user-friendly platform for utilizing the model, highlighting practical applications in real-world scenarios.



### Working App 
- Click on 'Choose file'
  ![Landing page](Media/Img1.png)
- Select any of the images, 
  ![Choose File](Media/Img2.png)
- Click on Upload
  ![Upload File](Media/Img3.png)
- Place the mask any any desired position, and then click "Inpaint"
  ![Masking Image](Media/Img4.png)
- The original image, masked image, and inpainted image are displayed
  ![Final Inpainting](Media/Img5.png)

