import json

sample_json = '{"_id":"5e7f9985a2f83fe195a5ca9e","index":0,"guid":"88b080e0-c9d7-4497-8b8c-20a8e0a23aca","isActive":true,"balance":"$2,367.88","picture":"http://placehold.it/32x32","age":34,"eyeColor":"blue","name":"AdkinsStark","gender":"male","company":"FORTEAN","email":"adkinsstark@fortean.com","phone":"+1(956)530-3060","address":"752HamptonAvenue,Felt,Guam,2849","about":"Quialiquipanimullamcoveniamaliquainconsequatipsumsunt.Pariaturdolorequiscillumeiusmodlaborisadcupidatatvelitoccaecatelitirurevoluptatesuntea.Inofficiaduisaliquipexercitationexadexercitationessefugiatvoluptateaddolor.Aliquipsintsintlaborumoccaecatconsequatvoluptateproidentminimetexercitationlaboreenim.Siteatemporetinconsequatsitipsum.","registered":"2019-01-18T08:16:56-06:-30","latitude":13.626154,"longitude":96.987674,"tags":["ea","magna","proident","non","exercitation","cupidatat","culpa"],"friends":[{"id":0,"name":"MasonBruce"},{"id":1,"name":"MosleyRocha"},{"id":2,"name":"MorseFrancis"}],"greeting":"Hello,AdkinsStark!Youhave4unreadmessages.","favoriteFruit":"banana"}'
sample_json_dict = json.loads(sample_json)
print(sample_json_dict['picture'])


sample_dict = {'friends': [{'id': 0, 'name': 'MasonBruce'}, {
    'id': 1, 'name': 'MosleyRocha'}, {'id': 2, 'name': 'MorseFrancis'}]}
sample_dict_json = json.dumps(sample_dict, indent=2, sort_keys=False)

print(sample_dict_json)


try:
    print(x)
except NameError:
    print('error')
finally:
    print('done')
