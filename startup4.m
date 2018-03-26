function startup()
% startup()
% --------------------------------------------------------
% Faster R-CNN
% Copyright (c) 2015, Shaoqing Ren
% Licensed under The MIT License [see LICENSE for details]
% --------------------------------------------------------

    curdir = fileparts(mfilename('fullpath'));
    addpath(genpath(fullfile(curdir, 'utils')));
    addpath(genpath(fullfile(curdir, 'functions')));
    addpath(genpath(fullfile(curdir, 'bin')));
    addpath(genpath(fullfile(curdir, 'experiments')));
    addpath(genpath(fullfile(curdir, 'imdb')));
    
    addpath(fullfile(curdir, 'datasets/caltech'));

    addpath(genpath(fullfile(curdir, 'external/toolbox')));

    caffe_path = fullfile(curdir, 'external', 'caffe', 'matlab');
    if exist(caffe_path, 'dir') == 0
        error('matcaffe is missing from external/caffe/matlab; See README.md');
    end
    addpath(genpath(caffe_path));

    mkdir_if_missing(fullfile(curdir, 'imdb', 'cache'));

    mkdir_if_missing(fullfile(curdir, 'output'));

    mkdir_if_missing(fullfile(curdir, 'models'));

    clear mex;
clear is_valid_handle; % to clear init_key
%run(fullfile(fileparts(fileparts(mfilename('fullpath'))), 'startup'));
%% -------------------- CONFIG --------------------
opts.caffe_version          = 'caffe_faster_rcnn';
opts.gpu_id                 = 4;
%opts.gpu_id                 = auto_select_gpu;

%
active_caffe_mex(opts.gpu_id, opts.caffe_version);
    
    fprintf('RPN_BF startup done\n');
end
