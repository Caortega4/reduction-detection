flist = getfeaturespec("C:\\Users\\carlo\\Research\\reductionFeatures.fss");
trackspecs = gettracklist('C:\\Research\\DownsampledRecordings\\ES\\');

% Iterate through the structs
for i = 1:length(trackspecs)
    % Split the filename into its base name and extension
    name = strsplit(trackspecs{1, i}.filename, '.');
    [~, features] = makeTrackMonster(trackspecs{1, i},flist);
    if trackspecs{1, i}.side == 'l'
        writematrix(features, strcat('C:\\Research\\features\\ES\\left_channel_',name{1},'features.csv'));
    else 
        writematrix(features, strcat('C:\\Research\\features\\ES\\right_channel_',name{1},'features.csv'));
    end
end