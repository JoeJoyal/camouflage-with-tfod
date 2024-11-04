# camouflage-with-tfod

<font color="green"> Configuration steps for TensorFlow object detection </font>

`STEP-1 Download the following content-`

1. Download v1.13.0 model.
2. Download the ssd_mobilenet_v1_coco model from the model zoo or any other model of your choice from Tensorflow 1 Detection Model Zoo.
3. Download Dataset $ utils.
4. Download labelImg tool for labeling Images.

Before extraction, you should have the following compressed files.

<font color="green"> STEP-2 Extract all the above zip files into tfod folder and remove the compressed files-` </font>


<font color="green">STEP-3 Creating virtual env using conda-` </font>

`Commands`
for specific python version
`conda create -n your_env_name python=3.7`
activate the environment
`conda activate your_env_name`

<font color="green">STEP-4 Install the following packages in your new environment-</font>
for GPU

`pip install pillow lxml Cython contextlib2 jupyter matplotlib pandas opencv-python tensorflow-gpu==1.15.0`

for CPU only

`pip install pillow lxml Cython contextlib2 jupyter matplotlib pandas opencv-python tensorflow==1.15.0`

<font color="green">STEP-5 Install protobuf using conda package manager-</font>

`conda install -c anaconda protobuf`

<font color="green">STEP-6 For protobuff to .py conversion download from a tool from here-</font>

For windows -> download source for other versions and OS - click here

Open command prompt and cd to research folder.

Now in the research folder run the following command-

`Now in the research folder run the following command-`

**For Linux or Mac**
`protoc object_detection/protos/*.proto --python_out=.`

**For Windows**
`protoc object_detection/protos/*.proto --python_out=.`