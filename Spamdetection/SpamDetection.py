import reimport pandas as pdimport numpy as npimport requestsfrom urlexpander import  expandimport urlexpanderimport multiprocessingimport mathdef FinalUrl(url):    try:        session = requests.Session()  # so connections are recycled        resp = session.get(url, allow_redirects=True)        return resp.url    except requests.exceptions.TooManyRedirects:        print('ConnectionError -- please wait 3 seconds')    except requests.exceptions.ConnectionError:        print('ChunkedEncodingError -- please wait 3 seconds')    except requests.exceptions.ConnectTimeout:        print('ChunkedEncodingError -- please wait 3 seconds')    return urldef run(i):    data=pd.read_csv('D:/study/Fake/url_'+str(i)+'.csv')    data=np.array(data)    data=data.tolist()    size = math.ceil(912135 / 40)    count=i*size    for i in data:        try:            count+=1            i[-1]=expand(i[-1])            print(count,' ',i[-1])        except requests.exceptions.TooManyRedirects:            print('ConnectionError -- please wait 3 seconds')        except requests.exceptions.ConnectionError:            print('ChunkedEncodingError -- please wait 3 seconds')        except requests.exceptions.ConnectTimeout:            print('ChunkedEncodingError -- please wait 3 seconds')        except:            print('unknow error')    return data