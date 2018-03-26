function dataset = caltech_val(dataset, usage)

switch usage
    case {'val'}
        dataset.imdb_test     = imdb_from_caltech('./datasets/caltech', 'val', false) ;
        dataset.roidb_test    = dataset.imdb_test.roidb_func(dataset.imdb_test, false);
    otherwise
        error('usage = ''val'' ');
end

end
