import os
from cryptography.fernet import Fernet

path_to_keyfile = r'keyfile.key'
datasample = '''#Isotropix_Clarisse_Clipboard_Serialization 0.94
Context "context" {
    copy_from "project://scene/context"
}
'''
if os.path.isfile(path_to_keyfile):
	print "-------------------------------------------------------"
	f = open(path_to_keyfile, 'r')
	key_store = f.readline()
	print "-------------------------------------------------------"
else:
	print "-------------------------------------------------------"
	print "no keys"


data = 'gAAAAABb_meb6KXRjpX51DVfCWi8rWnImT9itp6GI11fmD6ZIS1xfgmBHeMmX0Jq87PqN0eAbhd3ycxmrMQEenL09E-gZFOetThG6_U16hDhN7KLtX2wux2R3d3tMi7H8BHhuzzximRlCTwzH8OuCVF8xAijt2W7GBRhzHXloiyVoWJqUfainYHdoscij5ajKbFib75nLF0N6_VIxb98lsxUYC5WaVVH4u-nN9UjmHIUMt9AdEBQW5Q='
data2 = 'gAAAAABb_mhZsLF3Ws6ZWWA_-PS2g7n66A2l-UpWtFc4neHLb834X1zW084HpTH7GvMU53nF40LK5cZ29EdIHFrs5KItxBAA0DbMCbYi9dj4Tn2H-E6xDGNxQyHtt7Ipolg9lnasOZxuzYdXCFyt_JoaZp_b8h_6MmRtkDSHsHQ0dbPYz5I1TUghIYMxpie9Omhtjk0zHMgK3YAIyKCpbUHsR3NEcPZ4vDl1iJ-qTynwbR_LCffRM6sf2eIXExulyzwSvIri-6mw1RYItI4rH7_8D0VUirGZ0Uvu5EIk7tn0SuH_KEww1N-Q0GRee6Pw9VG9XUCKnpw1XuZTpWpQ4u-liMniZaJO8FrExwz7UQTrYMxeqew1-CdutitoCDGaQjjeedLYsz4z9kJricS1Vco8NsVeTlOeYbtia5ECm-Njwcx8mNPWW1r51thteEYa5SWQLsDJDe7qTicghih-tHyLZpjb28iMChSlV4uHKOHhy3Egf8NxL1cxZUR41v46AkWF0UTRf3ssAEJ8Lcn0j6yhvR9kYSuGdziv-XsaEllcauRSIrt3w4hERFBv4N6raH4e_QVx-ymryNp2yMG21HWmpWXkhNeyv8KvVt5lqs79ZdNb698vJivsEJz1pAeRLCOoUAcu6s7eFv1iTtzFrkE8ZT9YPHLyqv-3myw8oadAoOtWl7mRPmf7BY26mvmDw1NB8waLvNHK-ViR3SN8uXM_z5Tv1YMb9EL4aL1J5QcUfM2sM9Hj4FVmMv1V4zuuzfA9WXh3IhwMfApW7kFsyfCcdgrna7SgvcWncGMe8z6F0KojxX455MMsjLIoG1r3zeoPaF4ShevFoHrM00anqH0ZL21Z_0aLc-bve1MA2x4wCo4CNqF0o_ttE_xO3Wo0A-7afQdNtAHCIqsUrNugOY7YhsEtrMrHlJz7T4UugwQ57KRJv_ThD7zUC9CCGp1aFVSI1yV76Jzcg0BKosxyIglHnfKbubYP8m3fOUUbDDluQSDA7HDKxq1MoMyoKpggLuUgd8jldmW6pVBuP5V4NSY8FDQPMgT0bu9FBq4XL9e25Bqrx8tHwHUa6p9u5SoM9esNeDhuPVBcsW7-97Sz481AhEovej_ZeShocOcpIohF8Eta9ZNzAFQzh5r5yRuVLR_pQzFs7PCBLizWPcZbq-Ys7mYDkfReh6aCcc3EW5GFUe5styoTIL0qR0W_7zvw9vwLwx9sZzz3jDUH1dPTA82d8gnu1NqAsv4ckCf3jMFv2vpofHuxrT17LMGJYkUO0YeF5GAfoxAx6z2Zf7IgOqA4zQLdyvQvtNSRWqtXAQkdh6u26Zgv6dKADKU3laPmEYNQkRXcyVlmHWHUTpy0AaugY3krxIf5AMVOTUQkCeC3qwTcfBsYV3zrVWhdVRLyfKXlFGo-hLljQGtLNwJv_CnmemytmdPAkKjYF4w-wHDcdb7SLcqYwKMoT6LTO57-71JAf0GBPMUk'
d3 ='gAAAAABb_ml66IPEjqaTLtZP58i8b39GNFKUNqq3Vd4BUTWBEiDkUro7EBtf68F9lHGEujp0bCN5UBkOnz46qrcYJGw0KP5skBZa0ck-kA2FWB5YFzuc0Do='


d4=b'gAAAAABb_mm5oL-IEItGjigiD-LG3xLpef7f4VUXne0msKGZSl7lNI6OM7MUgUt8oefk4L3O81qYxJDU6Cd7hASYBSAXYl3BePtcUXChGYlcA9kuoc3vu0yohGcLd6eJV3thk2DfVGDFzpPeuj6mxWWDQLJFTQeAqdFntUJtI1VP9AGknje79atLbYWLtfJe5TNOiiDR-w38DAE6SnqAPsGPcJOX1yoQ2Nq6-stIu9WqAjcSa7OPH7ezI-5kWjvOBhSalGJUtyXOqm4_CHf9RoTtxTevvEk7n8d5I0P_NV5h1VUvuMBcJ2czSkgeTNgtAoa6pmn2YnkZvGQfA1KeQg6Utuq6o7P_KAuSAJ3QgCl52aqzAiUsy1cSIPs5J9tGb31FSuFciUuzlik_aJqVUqQ_wv5zc8UYWUCfVKIKxq18tHzL0yQ6e4VWjzDSISsdIARnfNHXvCtSaxTUR2sXfU6Vfa7HDr3GjB35ta-lHb3G5X3Y1r7weqw382lPwBsZvNSKeip2QZjiKQJq4rUsTinDpUbwxyOpeWhDXV4pSweS_SDwp_zdsX8W2cxFu15YrxlTF6B2OMdU0uRu2_qXlLjq7ykr3bNkoKc8EgQGSWxYdiZHg8kqfJMj_Th479Uv35GtVNi2sGw5UBNcWvACSQiBkbh6slv0HIZP4YNyEhdFqokYNdluMj-Tz3MWdeWy_jwUzx5rXqYvMRSaG--P0E9lOwd8--ww5uVfUX1cO-uUXUbgPWxBBxNmL4aUGu6URmoDbqBma4GoJ24Db87u4u1HmVivFt_auO0c2_jDCnSeUYn56j30DLxR9aP_ZDl-YENzYrd1sVQ2srvQAFT-8jDraR3yVadTSg6z-ZqleQE_KVyiMjFII8jJ_0sVOUYCgNUs5dFgidYoTSGwn9IUKQxV66IQeNsHH_TASsRyjAXQPCe5KuD9W78ZrlbYZq-f2a85S1LVudN0yNaib-NBhlHDnttYVnAYCi6HlrEWoReiqO4tJPXydxN0rqmKF9QsuGd5z591jsV17oZHjRAPuvfsHbjzUXpGCjQawKDkcy8zQyvIRO9lf4WBdnwtMvdQc57SE98iVsvBw9799WedFnmM2ccR98ouFTr4f3hxVCaFZantvdHyqWwQmnT1eptrc0JmQqXKu9CXrJk3zqPZ9UzmmEeelbrm9SKcxQuW0iIt7hlLbWfdD2lZ0ZyB1jD_7iCaKkQvIokK6aMKdZHrtlpKa7aWaMTlj8XHI1ZGhO6xFZWrpY_f3CtK6YYr5kIes4w09kyc273EwQlRdJS6kGCpstVmFVUqbisLLfy9AV5y4yxpphYtiefOM6LSzFZ5Wy0ijp1bYdMPEfuEB6R4B6i3GQom51DYaD_ftBDr6NgQxMWb14BQ6ONOFalebJghsUR0khb8bMS9exS1PVCmeji6d5rFgRbe9dxGQiFzb88KrGr8i0iSvcSSG-ABnOhyBAT8VRApkiKJhfAanAeSSXCgjMj10BOhMZtfriHlukd-ttS3bUiJjco='

try:
	cipher_suite = Fernet(key_store)
	#print datasample
	print "keystore is: ",key_store
	#cipher_text = cipher_suite.encrypt(data)
	plain_text = cipher_suite.decrypt(d4)
	print plain_text
except:
	print "!! NO KEY. Generate keys first to access DB."



