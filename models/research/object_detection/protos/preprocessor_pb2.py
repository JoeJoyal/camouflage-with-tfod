# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/preprocessor.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*object_detection/protos/preprocessor.proto\x12\x17object_detection.protos\"\xcb\x11\n\x11PreprocessingStep\x12\x42\n\x0fnormalize_image\x18\x01 \x01(\x0b\x32\'.object_detection.protos.NormalizeImageH\x00\x12O\n\x16random_horizontal_flip\x18\x02 \x01(\x0b\x32-.object_detection.protos.RandomHorizontalFlipH\x00\x12R\n\x18random_pixel_value_scale\x18\x03 \x01(\x0b\x32..object_detection.protos.RandomPixelValueScaleH\x00\x12G\n\x12random_image_scale\x18\x04 \x01(\x0b\x32).object_detection.protos.RandomImageScaleH\x00\x12\x46\n\x12random_rgb_to_gray\x18\x05 \x01(\x0b\x32(.object_detection.protos.RandomRGBtoGrayH\x00\x12S\n\x18random_adjust_brightness\x18\x06 \x01(\x0b\x32/.object_detection.protos.RandomAdjustBrightnessH\x00\x12O\n\x16random_adjust_contrast\x18\x07 \x01(\x0b\x32-.object_detection.protos.RandomAdjustContrastH\x00\x12\x45\n\x11random_adjust_hue\x18\x08 \x01(\x0b\x32(.object_detection.protos.RandomAdjustHueH\x00\x12S\n\x18random_adjust_saturation\x18\t \x01(\x0b\x32/.object_detection.protos.RandomAdjustSaturationH\x00\x12K\n\x14random_distort_color\x18\n \x01(\x0b\x32+.object_detection.protos.RandomDistortColorH\x00\x12I\n\x13random_jitter_boxes\x18\x0b \x01(\x0b\x32*.object_detection.protos.RandomJitterBoxesH\x00\x12\x45\n\x11random_crop_image\x18\x0c \x01(\x0b\x32(.object_detection.protos.RandomCropImageH\x00\x12\x43\n\x10random_pad_image\x18\r \x01(\x0b\x32\'.object_detection.protos.RandomPadImageH\x00\x12L\n\x15random_crop_pad_image\x18\x0e \x01(\x0b\x32+.object_detection.protos.RandomCropPadImageH\x00\x12W\n\x1brandom_crop_to_aspect_ratio\x18\x0f \x01(\x0b\x32\x30.object_detection.protos.RandomCropToAspectRatioH\x00\x12K\n\x14random_black_patches\x18\x10 \x01(\x0b\x32+.object_detection.protos.RandomBlackPatchesH\x00\x12K\n\x14random_resize_method\x18\x11 \x01(\x0b\x32+.object_detection.protos.RandomResizeMethodH\x00\x12\x61\n scale_boxes_to_pixel_coordinates\x18\x12 \x01(\x0b\x32\x35.object_detection.protos.ScaleBoxesToPixelCoordinatesH\x00\x12<\n\x0cresize_image\x18\x13 \x01(\x0b\x32$.object_detection.protos.ResizeImageH\x00\x12M\n\x15subtract_channel_mean\x18\x14 \x01(\x0b\x32,.object_detection.protos.SubtractChannelMeanH\x00\x12\x41\n\x0fssd_random_crop\x18\x15 \x01(\x0b\x32&.object_detection.protos.SSDRandomCropH\x00\x12H\n\x13ssd_random_crop_pad\x18\x16 \x01(\x0b\x32).object_detection.protos.SSDRandomCropPadH\x00\x12\x64\n\"ssd_random_crop_fixed_aspect_ratio\x18\x17 \x01(\x0b\x32\x36.object_detection.protos.SSDRandomCropFixedAspectRatioH\x00\x12k\n&ssd_random_crop_pad_fixed_aspect_ratio\x18\x18 \x01(\x0b\x32\x39.object_detection.protos.SSDRandomCropPadFixedAspectRatioH\x00\x12K\n\x14random_vertical_flip\x18\x19 \x01(\x0b\x32+.object_detection.protos.RandomVerticalFlipH\x00\x12\x46\n\x11random_rotation90\x18\x1a \x01(\x0b\x32).object_detection.protos.RandomRotation90H\x00\x12\x39\n\x0brgb_to_gray\x18\x1b \x01(\x0b\x32\".object_detection.protos.RGBtoGrayH\x00\x12_\n\x1f\x63onvert_class_logits_to_softmax\x18\x1c \x01(\x0b\x32\x34.object_detection.protos.ConvertClassLogitsToSoftmaxH\x00\x42\x14\n\x12preprocessing_step\"v\n\x0eNormalizeImage\x12\x17\n\x0foriginal_minval\x18\x01 \x01(\x02\x12\x17\n\x0foriginal_maxval\x18\x02 \x01(\x02\x12\x18\n\rtarget_minval\x18\x03 \x01(\x02:\x01\x30\x12\x18\n\rtarget_maxval\x18\x04 \x01(\x02:\x01\x31\"9\n\x14RandomHorizontalFlip\x12!\n\x19keypoint_flip_permutation\x18\x01 \x03(\x05\"7\n\x12RandomVerticalFlip\x12!\n\x19keypoint_flip_permutation\x18\x01 \x03(\x05\"\x12\n\x10RandomRotation90\"A\n\x15RandomPixelValueScale\x12\x13\n\x06minval\x18\x01 \x01(\x02:\x03\x30.9\x12\x13\n\x06maxval\x18\x02 \x01(\x02:\x03\x31.1\"L\n\x10RandomImageScale\x12\x1c\n\x0fmin_scale_ratio\x18\x01 \x01(\x02:\x03\x30.5\x12\x1a\n\x0fmax_scale_ratio\x18\x02 \x01(\x02:\x01\x32\"+\n\x0fRandomRGBtoGray\x12\x18\n\x0bprobability\x18\x01 \x01(\x02:\x03\x30.1\"0\n\x16RandomAdjustBrightness\x12\x16\n\tmax_delta\x18\x01 \x01(\x02:\x03\x30.2\"G\n\x14RandomAdjustContrast\x12\x16\n\tmin_delta\x18\x01 \x01(\x02:\x03\x30.8\x12\x17\n\tmax_delta\x18\x02 \x01(\x02:\x04\x31.25\"*\n\x0fRandomAdjustHue\x12\x17\n\tmax_delta\x18\x01 \x01(\x02:\x04\x30.02\"I\n\x16RandomAdjustSaturation\x12\x16\n\tmin_delta\x18\x01 \x01(\x02:\x03\x30.8\x12\x17\n\tmax_delta\x18\x02 \x01(\x02:\x04\x31.25\",\n\x12RandomDistortColor\x12\x16\n\x0e\x63olor_ordering\x18\x01 \x01(\x05\"(\n\x11RandomJitterBoxes\x12\x13\n\x05ratio\x18\x01 \x01(\x02:\x04\x30.05\"\xeb\x01\n\x0fRandomCropImage\x12\x1d\n\x12min_object_covered\x18\x01 \x01(\x02:\x01\x31\x12\x1e\n\x10min_aspect_ratio\x18\x02 \x01(\x02:\x04\x30.75\x12\x1e\n\x10max_aspect_ratio\x18\x03 \x01(\x02:\x04\x31.33\x12\x15\n\x08min_area\x18\x04 \x01(\x02:\x03\x30.1\x12\x13\n\x08max_area\x18\x05 \x01(\x02:\x01\x31\x12\x1b\n\x0eoverlap_thresh\x18\x06 \x01(\x02:\x03\x30.3\x12\x18\n\nclip_boxes\x18\x08 \x01(\x08:\x04true\x12\x16\n\x0brandom_coef\x18\x07 \x01(\x02:\x01\x30\"\x89\x01\n\x0eRandomPadImage\x12\x18\n\x10min_image_height\x18\x01 \x01(\x05\x12\x17\n\x0fmin_image_width\x18\x02 \x01(\x05\x12\x18\n\x10max_image_height\x18\x03 \x01(\x05\x12\x17\n\x0fmax_image_width\x18\x04 \x01(\x05\x12\x11\n\tpad_color\x18\x05 \x03(\x02\"\xbf\x02\n\x12RandomCropPadImage\x12\x1d\n\x12min_object_covered\x18\x01 \x01(\x02:\x01\x31\x12\x1e\n\x10min_aspect_ratio\x18\x02 \x01(\x02:\x04\x30.75\x12\x1e\n\x10max_aspect_ratio\x18\x03 \x01(\x02:\x04\x31.33\x12\x15\n\x08min_area\x18\x04 \x01(\x02:\x03\x30.1\x12\x13\n\x08max_area\x18\x05 \x01(\x02:\x01\x31\x12\x1b\n\x0eoverlap_thresh\x18\x06 \x01(\x02:\x03\x30.3\x12\x18\n\nclip_boxes\x18\x0b \x01(\x08:\x04true\x12\x16\n\x0brandom_coef\x18\x07 \x01(\x02:\x01\x30\x12\x1d\n\x15min_padded_size_ratio\x18\x08 \x03(\x02\x12\x1d\n\x15max_padded_size_ratio\x18\t \x03(\x02\x12\x11\n\tpad_color\x18\n \x03(\x02\"i\n\x17RandomCropToAspectRatio\x12\x17\n\x0c\x61spect_ratio\x18\x01 \x01(\x02:\x01\x31\x12\x1b\n\x0eoverlap_thresh\x18\x02 \x01(\x02:\x03\x30.3\x12\x18\n\nclip_boxes\x18\x03 \x01(\x08:\x04true\"o\n\x12RandomBlackPatches\x12\x1d\n\x11max_black_patches\x18\x01 \x01(\x05:\x02\x31\x30\x12\x18\n\x0bprobability\x18\x02 \x01(\x02:\x03\x30.5\x12 \n\x13size_to_image_ratio\x18\x03 \x01(\x02:\x03\x30.1\"A\n\x12RandomResizeMethod\x12\x15\n\rtarget_height\x18\x01 \x01(\x02\x12\x14\n\x0ctarget_width\x18\x02 \x01(\x02\"\x0b\n\tRGBtoGray\"\x1e\n\x1cScaleBoxesToPixelCoordinates\"\xc0\x01\n\x0bResizeImage\x12\x12\n\nnew_height\x18\x01 \x01(\x05\x12\x11\n\tnew_width\x18\x02 \x01(\x05\x12\x45\n\x06method\x18\x03 \x01(\x0e\x32+.object_detection.protos.ResizeImage.Method:\x08\x42ILINEAR\"C\n\x06Method\x12\x08\n\x04\x41REA\x10\x01\x12\x0b\n\x07\x42ICUBIC\x10\x02\x12\x0c\n\x08\x42ILINEAR\x10\x03\x12\x14\n\x10NEAREST_NEIGHBOR\x10\x04\"$\n\x13SubtractChannelMean\x12\r\n\x05means\x18\x01 \x03(\x02\"\xd3\x01\n\x16SSDRandomCropOperation\x12\x1a\n\x12min_object_covered\x18\x01 \x01(\x02\x12\x18\n\x10min_aspect_ratio\x18\x02 \x01(\x02\x12\x18\n\x10max_aspect_ratio\x18\x03 \x01(\x02\x12\x10\n\x08min_area\x18\x04 \x01(\x02\x12\x10\n\x08max_area\x18\x05 \x01(\x02\x12\x16\n\x0eoverlap_thresh\x18\x06 \x01(\x02\x12\x18\n\nclip_boxes\x18\x08 \x01(\x08:\x04true\x12\x13\n\x0brandom_coef\x18\x07 \x01(\x02\"T\n\rSSDRandomCrop\x12\x43\n\noperations\x18\x01 \x03(\x0b\x32/.object_detection.protos.SSDRandomCropOperation\"\xd3\x02\n\x19SSDRandomCropPadOperation\x12\x1a\n\x12min_object_covered\x18\x01 \x01(\x02\x12\x18\n\x10min_aspect_ratio\x18\x02 \x01(\x02\x12\x18\n\x10max_aspect_ratio\x18\x03 \x01(\x02\x12\x10\n\x08min_area\x18\x04 \x01(\x02\x12\x10\n\x08max_area\x18\x05 \x01(\x02\x12\x16\n\x0eoverlap_thresh\x18\x06 \x01(\x02\x12\x18\n\nclip_boxes\x18\r \x01(\x08:\x04true\x12\x13\n\x0brandom_coef\x18\x07 \x01(\x02\x12\x1d\n\x15min_padded_size_ratio\x18\x08 \x03(\x02\x12\x1d\n\x15max_padded_size_ratio\x18\t \x03(\x02\x12\x13\n\x0bpad_color_r\x18\n \x01(\x02\x12\x13\n\x0bpad_color_g\x18\x0b \x01(\x02\x12\x13\n\x0bpad_color_b\x18\x0c \x01(\x02\"Z\n\x10SSDRandomCropPad\x12\x46\n\noperations\x18\x01 \x03(\x0b\x32\x32.object_detection.protos.SSDRandomCropPadOperation\"\xaf\x01\n&SSDRandomCropFixedAspectRatioOperation\x12\x1a\n\x12min_object_covered\x18\x01 \x01(\x02\x12\x10\n\x08min_area\x18\x04 \x01(\x02\x12\x10\n\x08max_area\x18\x05 \x01(\x02\x12\x16\n\x0eoverlap_thresh\x18\x06 \x01(\x02\x12\x18\n\nclip_boxes\x18\x08 \x01(\x08:\x04true\x12\x13\n\x0brandom_coef\x18\x07 \x01(\x02\"\x8d\x01\n\x1dSSDRandomCropFixedAspectRatio\x12S\n\noperations\x18\x01 \x03(\x0b\x32?.object_detection.protos.SSDRandomCropFixedAspectRatioOperation\x12\x17\n\x0c\x61spect_ratio\x18\x02 \x01(\x02:\x01\x31\"\xe6\x01\n)SSDRandomCropPadFixedAspectRatioOperation\x12\x1a\n\x12min_object_covered\x18\x01 \x01(\x02\x12\x18\n\x10min_aspect_ratio\x18\x02 \x01(\x02\x12\x18\n\x10max_aspect_ratio\x18\x03 \x01(\x02\x12\x10\n\x08min_area\x18\x04 \x01(\x02\x12\x10\n\x08max_area\x18\x05 \x01(\x02\x12\x16\n\x0eoverlap_thresh\x18\x06 \x01(\x02\x12\x18\n\nclip_boxes\x18\x08 \x01(\x08:\x04true\x12\x13\n\x0brandom_coef\x18\x07 \x01(\x02\"\xd1\x01\n SSDRandomCropPadFixedAspectRatio\x12V\n\noperations\x18\x01 \x03(\x0b\x32\x42.object_detection.protos.SSDRandomCropPadFixedAspectRatioOperation\x12\x17\n\x0c\x61spect_ratio\x18\x02 \x01(\x02:\x01\x31\x12\x1d\n\x15min_padded_size_ratio\x18\x03 \x03(\x02\x12\x1d\n\x15max_padded_size_ratio\x18\x04 \x03(\x02\"5\n\x1b\x43onvertClassLogitsToSoftmax\x12\x16\n\x0btemperature\x18\x01 \x01(\x02:\x01\x31')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'object_detection.protos.preprocessor_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PREPROCESSINGSTEP._serialized_start=72
  _PREPROCESSINGSTEP._serialized_end=2323
  _NORMALIZEIMAGE._serialized_start=2325
  _NORMALIZEIMAGE._serialized_end=2443
  _RANDOMHORIZONTALFLIP._serialized_start=2445
  _RANDOMHORIZONTALFLIP._serialized_end=2502
  _RANDOMVERTICALFLIP._serialized_start=2504
  _RANDOMVERTICALFLIP._serialized_end=2559
  _RANDOMROTATION90._serialized_start=2561
  _RANDOMROTATION90._serialized_end=2579
  _RANDOMPIXELVALUESCALE._serialized_start=2581
  _RANDOMPIXELVALUESCALE._serialized_end=2646
  _RANDOMIMAGESCALE._serialized_start=2648
  _RANDOMIMAGESCALE._serialized_end=2724
  _RANDOMRGBTOGRAY._serialized_start=2726
  _RANDOMRGBTOGRAY._serialized_end=2769
  _RANDOMADJUSTBRIGHTNESS._serialized_start=2771
  _RANDOMADJUSTBRIGHTNESS._serialized_end=2819
  _RANDOMADJUSTCONTRAST._serialized_start=2821
  _RANDOMADJUSTCONTRAST._serialized_end=2892
  _RANDOMADJUSTHUE._serialized_start=2894
  _RANDOMADJUSTHUE._serialized_end=2936
  _RANDOMADJUSTSATURATION._serialized_start=2938
  _RANDOMADJUSTSATURATION._serialized_end=3011
  _RANDOMDISTORTCOLOR._serialized_start=3013
  _RANDOMDISTORTCOLOR._serialized_end=3057
  _RANDOMJITTERBOXES._serialized_start=3059
  _RANDOMJITTERBOXES._serialized_end=3099
  _RANDOMCROPIMAGE._serialized_start=3102
  _RANDOMCROPIMAGE._serialized_end=3337
  _RANDOMPADIMAGE._serialized_start=3340
  _RANDOMPADIMAGE._serialized_end=3477
  _RANDOMCROPPADIMAGE._serialized_start=3480
  _RANDOMCROPPADIMAGE._serialized_end=3799
  _RANDOMCROPTOASPECTRATIO._serialized_start=3801
  _RANDOMCROPTOASPECTRATIO._serialized_end=3906
  _RANDOMBLACKPATCHES._serialized_start=3908
  _RANDOMBLACKPATCHES._serialized_end=4019
  _RANDOMRESIZEMETHOD._serialized_start=4021
  _RANDOMRESIZEMETHOD._serialized_end=4086
  _RGBTOGRAY._serialized_start=4088
  _RGBTOGRAY._serialized_end=4099
  _SCALEBOXESTOPIXELCOORDINATES._serialized_start=4101
  _SCALEBOXESTOPIXELCOORDINATES._serialized_end=4131
  _RESIZEIMAGE._serialized_start=4134
  _RESIZEIMAGE._serialized_end=4326
  _RESIZEIMAGE_METHOD._serialized_start=4259
  _RESIZEIMAGE_METHOD._serialized_end=4326
  _SUBTRACTCHANNELMEAN._serialized_start=4328
  _SUBTRACTCHANNELMEAN._serialized_end=4364
  _SSDRANDOMCROPOPERATION._serialized_start=4367
  _SSDRANDOMCROPOPERATION._serialized_end=4578
  _SSDRANDOMCROP._serialized_start=4580
  _SSDRANDOMCROP._serialized_end=4664
  _SSDRANDOMCROPPADOPERATION._serialized_start=4667
  _SSDRANDOMCROPPADOPERATION._serialized_end=5006
  _SSDRANDOMCROPPAD._serialized_start=5008
  _SSDRANDOMCROPPAD._serialized_end=5098
  _SSDRANDOMCROPFIXEDASPECTRATIOOPERATION._serialized_start=5101
  _SSDRANDOMCROPFIXEDASPECTRATIOOPERATION._serialized_end=5276
  _SSDRANDOMCROPFIXEDASPECTRATIO._serialized_start=5279
  _SSDRANDOMCROPFIXEDASPECTRATIO._serialized_end=5420
  _SSDRANDOMCROPPADFIXEDASPECTRATIOOPERATION._serialized_start=5423
  _SSDRANDOMCROPPADFIXEDASPECTRATIOOPERATION._serialized_end=5653
  _SSDRANDOMCROPPADFIXEDASPECTRATIO._serialized_start=5656
  _SSDRANDOMCROPPADFIXEDASPECTRATIO._serialized_end=5865
  _CONVERTCLASSLOGITSTOSOFTMAX._serialized_start=5867
  _CONVERTCLASSLOGITSTOSOFTMAX._serialized_end=5920
# @@protoc_insertion_point(module_scope)
