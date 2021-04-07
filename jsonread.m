clear
i = 1;
while 1
    try
        all_files = py.glob.glob('/openpose/output/*.json');%%outputのファイル数確認
        cella = cellfun(@char,cell(all_files),'UniformOutput',false);%%jsonファイル配列化
        jfilea = cella{i};%%ファイル一つ選択
    
        %%ファイル開いてデータ分ける%%
        open_file = py.open(jfilea,'r');
        load_file = py.json.load(open_file);
        load_Mfile = struct(load_file);
        partCandidates = load_Mfile.part_candidates;
        parts_num = partCandidates{1};
        parts_number = parts_num{'0'};%%欲しい場所の数に変える
        %%座標データ
        partx = parts_number(1);
        party = parts_number(2);
        cPartx = cell(partx);
        cParty = cell(party);
        X = cellfun(@double,cPartx)
        Y = cellfun(@double,cParty)
    
        i = i + 1;
    catch IndexError
        disp('Waiting for the file to be created!')
    end

end    
   
