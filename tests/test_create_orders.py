import allure
import requests
from http import HTTPStatus
from data.endpoints import Endpoints
from data.generator.generator import Generator
from modules.create_order_module import CreateOrderModule
from utils.assertions import Assertions
from utils.schemas.create_orders_schema.request_schema import CreateOrdesRequestSchema
from utils.schemas.create_orders_schema.response_schema import CreateOrderResponseSchema
from utils.validate import Validate


class TestCreateOrders:
    generator = Generator()
    module = CreateOrderModule()
    endpoint = Endpoints()
    validate = Validate()
    assertion = Assertions()

    def test_create_orders(self, create_endpoint, get_auth_token):
        user_info = next(self.generator.create_order_data())
        request_body = self.module.create_request_body(
            schema=CreateOrdesRequestSchema,
            data_class_instance=user_info
        )
        response = requests.post(
            url=f"{self.endpoint.base_url}{self.endpoint.orders_url}",
            data=request_body,
            headers=get_auth_token
        )
        self.validate.validate(response, CreateOrderResponseSchema)
        self.assertion.assert_status_code(response, HTTPStatus.CREATED)

    def test_create_orders1(self, create_endpoint, get_auth_token):
        with allure.step("Generate test data for order creation"):
            user_info = next(self.generator.create_order_data())

        with allure.step("Prepare request body"):
            request_body = self.module.create_request_body(
                schema=CreateOrdesRequestSchema,
                data_class_instance=user_info
            )

        with allure.step("Send POST request to create order"):
            response = requests.post(
                url=f"{self.endpoint.base_url}{self.endpoint.orders_url}",
                data=request_body,
                headers=get_auth_token
            )

        with allure.step("Validate response schema"):
            self.validate.validate(response, CreateOrderResponseSchema)

        with allure.step("Verify status code is 201 CREATED"):
            self.assertion.assert_status_code(response, HTTPStatus.CREATED)

        print(response.request.url)
        print(response.request.body)
        print(response.status_code)
        print(response.json())