@app.route('/api/sep/2.0/insert_1',methods=['POST'])
def sep_insert():
    end_point='SEP/2.0/insert'
    method = 'post'
    payload = {
        "request":{
            "t_sep":{
                "noKartu":"0002084341004",
                "tglSep":"2022-01-17",#Date Now
                "ppkPelayanan":kodeppk,#Static
                "jnsPelayanan":"2", #1.RI, 2.RJ
                "klsRawat":{
                    "klsRawatHak":"3", 
                    "klsRawatNaik":"", #1.VVIP, 2.VIP, 3.Kelas 1, 4.Kelas 2, 5.Kelas 3, 6.ICCU, 7.ICU
                    "pembiayaan":"", #1. Pribadi, 2. Pemberi Kerja, 3. Asuransi Kesehatan Tambahan. diisi jika naik kelas rawat
                    "penanggungJawab":"" # diisi jika naik kelas rawat
                },
                "noMR":"135635",
                "rujukan":{
                    "asalRujukan":"2", #1.Faskes 1, 2. Faskes 2(RS)
                    "tglRujukan":"2021-12-03", #Tanggal Rujukan
                    "noRujukan":"", #No Rujukan
                    "ppkRujukan":kodeppk # provUmum => kdProvider
                },
                "catatan":"testinsert RJ", # ??
                "diagAwal":"E12", #Diagnosa => kode
                "poli":{
                    "tujuan":"IGD", #Poli Rujukan => kode
                    "eksekutif":"0"
                },
                "cob":{
                    "cob":"0"
                },
                "katarak":{
                    "katarak":"0"
                },
                "jaminan":{
                    "lakaLantas":"0",
                    "penjamin":{
                        "tglKejadian":"",
                        "keterangan":"",
                        "suplesi":{
                            "suplesi":"0",
                            "noSepSuplesi":"",
                            "lokasiLaka":{
                                "kdPropinsi":"",
                                "kdKabupaten":"",
                                "kdKecamatan":""
                            }
                        }
                    }
                },
                "tujuanKunj":"0",
                "flagProcedure":"", # Kosong Tujuan 0
                "kdPenunjang":"",
                "assesmentPel":"",
                "skdp":{
                    "noSurat":"0301R0110721K000021", # ????
                    "kodeDPJP":"22214" #GET DOKTER
                },
                "dpjpLayan":"22214", #GET DOKTER => EMPTY RI
                "noTelp":"081111111101", #No Telp Pasien
                "user":"Coba Ws" #USer
            } 
        }
    }
    return BpjsController.bridging(end_point,method,payload)


@app.route('/api/sep/2.0/insert',methods=['POST'])
def sep_insert2():
    data = request.get_json()
    today = str(datetime.today().strftime('%Y-%m-%d'))
    datas = {
        'noKartu':data['noKartu'],
        'tglSep':today,
        'ppkPelayanan':kodeppk,
        'klsRawat_klsRawatHak':data['klsRawat_klsRawatHak'],
        'klsRawat_klsRawatNaik':data['klsRawat_klsRawatNaik'],
        'klsRawat_pembiayaan':data['klsRawat_pembiayaan'],
        'klsRawat_penanggung_jawab':data['klsRawat_penanggung_jawab'],
        'noMR':data['noMR'],
        'rujukan_asalRujukan':data['rujukan_asalRujukan'],
        'rujukan_tglRujukan':data['rujukan_tglRujukan'],
        'rujukan_noRujukan':data['rujukan_noRujukan'],
        'rujukan_ppkRujukan':data['rujukan_ppkRujukan'],
        'catatan':data['catatan'],
        'diagAwal':data['diagAwal'],
        'poli_tujuan':data['poli_tujuan'],
        'poli_eksekutif':data['poli_eksekutif'],
        'cob':data['cob'],
        'katarak_katarak':data['katarak_katarak'],
        'jaminan_lakaLantas':data['jaminan_lakaLantas'],
        'jaminan_penjamin_tglKejadian':data['jaminan_penjamin_tglKejadian'],
        'jaminan_penjamin_keterangan':data['jaminan_penjamin_keterangan'],
        'jaminan_penjamin_suplesi_suplesi':data['jaminan_penjamin_suplesi_suplesi'],
        'jaminan_penjamin_suplesi_noSepSuplesi':data['jaminan_penjamin_suplesi_noSepSuplesi'],
        'jaminan_penjamin_suplesi_lokasiLaka_kdPropinsi':data['jaminan_penjamin_suplesi_lokasiLaka_kdPropinsi'],
        'jaminan_penjamin_suplesi_lokasiLaka_kdKabupaten':data['jaminan_penjamin_suplesi_lokasiLaka_kdKabupaten'],
        'jaminan_penjamin_suplesi_lokasiLaka_kdKecamatan':data['jaminan_penjamin_suplesi_lokasiLaka_kdKecamatan'],
        'tujuanKunj':data['tujuanKunj'],
        'flagProcedure':data['flagProcedure'],
        'kdPenunjang':data['kdPenunjang'],
        'assesmentPel':data['assesmentPel'],
        'skdp_noSurat':data['skdp_noSurat'],
        'skdp_kodeDPJP':data['skdp_kodeDPJP'],
        'dpjpLayan':data['dpjpLayan'],
        'noTelp':data['noTelp'],
        'user':data['user'],
    }

    end_point='SEP/2.0/insert'
    method = 'post'
    # payload = payload_Insert_SEP(datas)
    return datas['user']

def payload_Insert_SEP(data):
    payload = {
        "request":{
            "t_sep":{
                "noKartu":data['noKartu'],
                "tglSep":data['today'],#Date Now
                "ppkPelayanan":kodeppk,#Static
                "jnsPelayanan":data['jnsPelayanan'], #1.RI, 2.RJ
                "klsRawat":{
                    "klsRawatHak":data['klsRawat_klsRawatHak'], 
                    "klsRawatNaik":data['klsRawat_klsRawatNaik'], #1.VVIP, 2.VIP, 3.Kelas 1, 4.Kelas 2, 5.Kelas 3, 6.ICCU, 7.ICU
                    "pembiayaan":data['klsRawat_pembiayaan'], #1. Pribadi, 2. Pemberi Kerja, 3. Asuransi Kesehatan Tambahan. diisi jika naik kelas rawat
                    "penanggungJawab":data['klsRawat_penanggungJawab'] # diisi jika naik kelas rawat
                },
                "noMR":"135635",
                "rujukan":{
                    "asalRujukan":"1", #1.Faskes 1, 2. Faskes 2(RS)
                    "tglRujukan":"2021-12-03", #Tanggal Rujukan
                    "noRujukan":"080209020122P000007", #No Rujukan
                    "ppkRujukan":"08070802" # provUmum => kdProvider
                },
                "catatan":"testinsert RJ", # ??
                "diagAwal":"E12", #Diagnosa => kode
                "poli":{
                    "tujuan":"BED", #Poli Rujukan => kode
                    "eksekutif":"0"
                },
                "cob":{
                    "cob":"0"
                },
                "katarak":{
                    "katarak":"0"
                },
                "jaminan":{
                    "lakaLantas":"0",
                    "penjamin":{
                        "tglKejadian":"",
                        "keterangan":"",
                        "suplesi":{
                            "suplesi":"0",
                            "noSepSuplesi":"",
                            "lokasiLaka":{
                                "kdPropinsi":"",
                                "kdKabupaten":"",
                                "kdKecamatan":""
                            }
                        }
                    }
                },
                "tujuanKunj":"0",
                "flagProcedure":"",
                "kdPenunjang":"",
                "assesmentPel":"",
                "skdp":{
                    "noSurat":"0301R0110721K000021", # ????
                    "kodeDPJP":"22214" #GET DOKTER
                },
                "dpjpLayan":"22214", #GET DOKTER => EMPTY RI
                "noTelp":"081111111101", #No Telp Pasien
                "user":"Coba Ws" #User
            } 
        }
    }
    return payload
    
    # sep_respons=sepRequest(
    #     noKartu='12344',
    #     tglSep='2022-01-17'
    # )
    # db.session.add(sep_respons)
    # db.session.commit()

    # return datas['noKartu']

    # data={

    # }

    
   
    # return BpjsController.bridging(end_point,method,payload)