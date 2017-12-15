# Different loss weight

# --------------------------
# Inception hyper-parameter
# --------------------------
content_weight = 1e0
style_weight = 1e4
tv_weight = 2e2

# Related input/output path
model_path = './model/'
model_name = 'chi.ckpt'
style_path = './img/style/'
style_name = 'star.jpg'
content_path = 'data/train2014'
video_path = './video/'
video_input_name = '20977333_328662897561035_2692550031910633472_n.mp4'
video_output_name = 'res.mp4'
vgg_path = './imagenet-vgg-verydeep-19.mat'
image_shape = (1, 224, 400, 3)

# Parameter about training
iteration = 2000
style_pretrain_iteration = 2000
batch_size = 8
num_example = 64
evaluate_period = 10

# Use multi-process
adopt_multiprocess = False
device_list = ['/gpu:0', '/gpu:0']