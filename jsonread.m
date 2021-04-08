clear all
i = 1;
while 1
    try
        all_files = py.glob.glob('/openpose/output/*.json');%outputのファイル確認
        cella = cellfun(@char,cell(all_files),'UniformOutput',false);%jsonファイル配列化
        jfilea = cella{i};%ファイル一つ選択
    
        %ファイル開いてデータ分ける%%
        open_file = py.open(jfilea,'r');
        load_file = py.json.load(open_file);
        load_Mfile = struct(load_file);
        partCandidates = load_Mfile.part_candidates;
        parts_num = partCandidates{1};
        parts_number = parts_num{'1'};
        cellP = cellfun(@double,cell(parts_number));
        A = isempty(cellP);%空の配列確認
        
        %%座標データ
        partx = parts_number(1);
        party = parts_number(2);
        cPartx = cell(partx);
        cParty = cell(party);
        X = cellfun(@double,cPartx)
        Y = cellfun(@double,cParty)
        plot(X,Y,'g')
        i = i + 1;         
    catch IndexError
        if A == 1
            i = i + 1;
        elseif A == 0     
            disp('Waiting for the file to be created!')            
        end
    end
end    
