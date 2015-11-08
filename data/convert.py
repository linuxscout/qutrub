from triverbtable import *
def create_triverbtable():
	for item in TriVerbTable.keys():
		for key in item.keys() :
			liste=item[key];
			for element in liste:
				root=element['root'];
				bab=element['bab']
				transitive=element['transitive']
				haraka=element['haraka']
				vocverb=key;
				element['verb']=vocverb;
				id=vocverb+str(bab);
				element['id']=id;
				print 	element;
create_triverbtable()
