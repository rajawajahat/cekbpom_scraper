from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import mysql.connector
import json

# Create your views here.


def home(request):
    return render(request, 'front.html', {})
    
    
    
def query_by_product(request):
    
    json_data = json.loads(request.POST.get('data'))
    # print(json_data)
    
    if json_data["value"]:
    
        """
        Making connection and inserting data into database.
        """  
        connection = mysql.connector.connect(host='localhost',database='License',user='root',password='root')
        cursor = connection.cursor()

        # Sql parametrized query
        sql_select_query = """select * from ProductsData where Product = %s"""
        
        # set variable in query
        cursor.execute(sql_select_query, (json_data["value"],))
        
        # fetch result
        records = cursor.fetchall()
       
        # Closing the connection
        connection.commit()
        connection.close()
        
        # Converting data to joson
        json_data = json.dumps(records)
        
        return JsonResponse({"records":json_data})
       
def query_by_product_name(request):

    json_data = json.loads(request.POST.get('data'))
    # print(json_data)
    
    if json_data["value"]:
    
        """
        Making connection and inserting data into database.
        """  
        connection = mysql.connector.connect(host='localhost',database='License',user='root',password='root')
        cursor = connection.cursor()

        # Sql parametrized query
        sql_select_query = """select * from ProductsData where ProductName = %s"""
        
        # set variable in query
        cursor.execute(sql_select_query, (json_data["value"],))
        
        # fetch result
        records = cursor.fetchall()
       
        # Closing the connection
        connection.commit()
        connection.close()
        
        # Converting data to joson
        json_data = json.dumps(records)
        
        return JsonResponse({"records":json_data})


def query_by_brand(request):
    
    json_data = json.loads(request.POST.get('data'))
    # print(json_data)
    
    if json_data["value"]:
    
        """
        Making connection and inserting data into database.
        """  
        connection = mysql.connector.connect(host='localhost',database='License',user='root',password='root')
        cursor = connection.cursor()

        # Sql parametrized query
        sql_select_query = """select * from ProductsData where Brand = %s"""
        
        # set variable in query
        cursor.execute(sql_select_query, (json_data["value"],))
        
        # fetch result
        records = cursor.fetchall()
       
        # Closing the connection
        connection.commit()
        connection.close()
        
        # Converting data to joson
        json_data = json.dumps(records)
        
        return JsonResponse({"records":json_data})


def query_by_registrant(request):
    
    json_data = json.loads(request.POST.get('data'))
    # print(json_data)
    
    if json_data["value"]:
    
        """
        Making connection and inserting data into database.
        """  
        connection = mysql.connector.connect(host='localhost',database='License',user='root',password='root')
        cursor = connection.cursor()

        # Sql parametrized query
        sql_select_query = """select * from ProductsData where Registrant = %s"""
        
        # set variable in query
        cursor.execute(sql_select_query, (json_data["value"],))
        
        # fetch result
        records = cursor.fetchall()
       
        # Closing the connection
        connection.commit()
        connection.close()
        
        # Converting data to joson
        json_data = json.dumps(records)
        
        return JsonResponse({"records":json_data})


def query_by_producer(request):
    
    json_data = json.loads(request.POST.get('data'))
    # print(json_data)
    
    if json_data["value"]:
    
        """
        Making connection and inserting data into database.
        """  
        connection = mysql.connector.connect(host='localhost',database='License',user='root',password='root')
        cursor = connection.cursor()

        # Sql parametrized query
        sql_select_query = """select * from ProductsData where Company = %s"""
        
        # set variable in query
        cursor.execute(sql_select_query, (json_data["value"],))
        
        # fetch result
        records = cursor.fetchall()
       
        # Closing the connection
        connection.commit()
        connection.close()
        
        # Converting data to joson
        json_data = json.dumps(records)
        
        return JsonResponse({"records":json_data})


def query_by_validity(request):
    
    json_data = json.loads(request.POST.get('data'))
    # print(json_data)
    
    if json_data["value"]:
    
        """
        Making connection and inserting data into database.
        """  
        connection = mysql.connector.connect(host='localhost',database='License',user='root',password='root')
        cursor = connection.cursor()

        # Sql parametrized query
        sql_select_query = """select * from ProductsData where ValidDate = %s"""
        
        # set variable in query
        cursor.execute(sql_select_query, (json_data["value"],))
        
        # fetch result
        records = cursor.fetchall()
       
        # Closing the connection
        connection.commit()
        connection.close()
        
        # Converting data to joson
        json_data = json.dumps(records)
        
        return JsonResponse({"records":json_data})

