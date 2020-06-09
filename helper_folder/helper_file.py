from flask import request


def clean_update(request_form):
    return {
        "rec_name": request.form.get('rec_name'),
        "rec_aut": request.form.get('rec_aut'),
        "rec_type": request.form.get('rec_type'),
        "rec_diff": request.form.get('rec_diff'),
        "rec_time_h": request.form.get('rec_time_h'),
        "rec_time_m": request.form.get('rec_time_m'),
        "rec_serve": request.form.get('rec_serve'),
        "rec_ing_n1": request.form.get('rec_ing_n1'),
        "rec_ing_a1": request.form.get('rec_ing_a1'),
        "rec_ing_u1": request.form.get('rec_ing_u1'),
        "rec_ing_n2": request.form.get('rec_ing_n2'),
        "rec_ing_a2": request.form.get('rec_ing_a2'),
        "rec_ing_u2": request.form.get('rec_ing_u2'),
        "rec_ing_n3": request.form.get('rec_ing_n3'),
        "rec_ing_a3": request.form.get('rec_ing_a3'),
        "rec_ing_u3": request.form.get('rec_ing_u3'),
        "rec_ing_n4": request.form.get('rec_ing_n4'),
        "rec_ing_a4": request.form.get('rec_ing_a4'),
        "rec_ing_u4": request.form.get('rec_ing_u4'),
        "rec_ing_n5": request.form.get('rec_ing_n5'),
        "rec_ing_a5": request.form.get('rec_ing_a5'),
        "rec_ing_u5": request.form.get('rec_ing_u5'),
        "rec_ing_n6": request.form.get('rec_ing_n6'),
        "rec_ing_a6": request.form.get('rec_ing_a6'),
        "rec_ing_u6": request.form.get('rec_ing_u6'),
        "rec_ing_n7": request.form.get('rec_ing_n7'),
        "rec_ing_a7": request.form.get('rec_ing_a7'),
        "rec_ing_u7": request.form.get('rec_ing_u7'),
        "rec_ing_n8": request.form.get('rec_ing_n8'),
        "rec_ing_a8": request.form.get('rec_ing_a8'),
        "rec_ing_u8": request.form.get('rec_ing_u8'),
        "rec_ing_n9": request.form.get('rec_ing_n9'),
        "rec_ing_a9": request.form.get('rec_ing_a9'),
        "rec_ing_u9": request.form.get('rec_ing_u9'),
        "rec_ing_n10": request.form.get('rec_ing_n10'),
        "rec_ing_a10": request.form.get('rec_ing_a10'),
        "rec_ing_u10": request.form.get('rec_ing_u10'),
        "rec_ing_n11": request.form.get('rec_ing_n11'),
        "rec_ing_a11": request.form.get('rec_ing_a11'),
        "rec_ing_u11": request.form.get('rec_ing_u11'),
        "rec_ing_n12": request.form.get('rec_ing_n12'),
        "rec_ing_a12": request.form.get('rec_ing_a12'),
        "rec_ing_u12": request.form.get('rec_ing_u12'),
        "rec_ing_n13": request.form.get('rec_ing_n13'),
        "rec_ing_a13": request.form.get('rec_ing_a13'),
        "rec_ing_u13": request.form.get('rec_ing_u13'),
        "rec_ing_n14": request.form.get('rec_ing_n14'),
        "rec_ing_a14": request.form.get('rec_ing_a14'),
        "rec_ing_u14": request.form.get('rec_ing_u14'),
        "rec_ing_n15": request.form.get('rec_ing_n15'),
        "rec_ing_a15": request.form.get('rec_ing_a15'),
        "rec_ing_u15": request.form.get('rec_ing_u15'),
        "rec_step1": request.form.get('rec_step1'),
        "rec_step2": request.form.get('rec_step2'),
        "rec_step3": request.form.get('rec_step3'),
        "rec_step4": request.form.get('rec_step4'),
        "rec_step5": request.form.get('rec_step5'),
        "rec_step6": request.form.get('rec_step6'),
        "rec_step7": request.form.get('rec_step7'),
        "rec_step8": request.form.get('rec_step8'),
        "rec_step9": request.form.get('rec_step9'),
        "rec_step10": request.form.get('rec_step10'),
        "rec_step11": request.form.get('rec_step11'),
        "rec_step12": request.form.get('rec_step12'),
        "rec_step13": request.form.get('rec_step13'),
        "rec_step14": request.form.get('rec_step14'),
        "rec_step15": request.form.get('rec_step15'),
        "rec_pic": request.form.get('rec_pic')
    }