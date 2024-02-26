import os
import uuid
from app import app, db, uploadconfig
from flask import Flask, request, jsonify
from app.models.Transaction import Transaction
from app.models.Transaction_Detail import Transaction_Detail
from app.res.response import get_success, bad_request, post_success

def get():
    transaction = Transaction.query.all()
    if transaction:
        data = formatarray(transaction)
        return get_success(data, "Data berhasil ditampilkan")
    return bad_request([], "Transaksi tidak ditemukan")

def detail_transaction(id):
    transaction = Transaction.query.filter_by(id=id).first()
    detail = Transaction_Detail.query.filter_by(transaction_id=transaction.id)
    
    if not transaction:
        return bad_request([], "Tidak ada transaksi di ID ini")
    
    datatransaction = formatTransaction(detail)
    data = singleDetailTransaction(transaction, datatransaction)
    return get_success(data, "Data berhasil ditampilkan")

# Print out the json for Transaction
def formatarray(data):
    array = []
    for i in data:
        array.append(singleObject(i))
        
    return array

def singleObject(data):
    data = {
        'id': data.id,
        'transaction_no': data.transaction_no,
        'total_amount': data.total_amount,
        'active': data.active,
        'created_user': data.created_user,
        'created_date': data.created_date,
        'updated_user': data.updated_user,
        'updated_date': data.updated_date
    }

    return data

# Print out the json for Transaction Detail
def formatTransaction(data):
    array = []
    for i in data:
        array.append(singleDetailTransaction(i))
        
    return array

def singleDetailTransaction(data):
    data = {
        'id': data.id,
        'transaction_id': data.transaction_id,
        'product_variant_id': data.product_variant_id,
        'price': data.price,
        'qty': data.qty,
        'subtotal': data.subtotal,
        'active': data.active,
        'created_user': data.created_user,
        'created_date': data.created_date,
        'updated_user': data.updated_user,
        'updated_date': data.updated_date
    }
    
    return data