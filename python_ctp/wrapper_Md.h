/*

A wrapper for CTP's Api library
author: Lvsoft@gmail.com
date: 2013-11-17

This file is part of python-ctp library

python-ctp is free software; you can redistribute it and/or modify it
under the terms of the GUL Lesser General Public License as published
by the Free Software Foundation; either version 2.1 of the License, or
(at your option) any later version.

python-ctp is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY of FITNESS FOR A PARTICULAR PURPOSE. See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along the python-ctp; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301 USA
*/

#ifndef WRAPPER_H
#define WRAPPER_H

#include <Python.h>
#include "ThostFtdcMdApiSSE.h"

class MySpiWrapper : public CZQThostFtdcMdSpi
{
 public:
  MySpiWrapper(PyObject * parent);

  virtual void OnFrontDisconnected(int nReason);
  virtual void OnRspUserLogout(CZQThostFtdcUserLogoutField* pUserLogout, CZQThostFtdcRspInfoField* pRspInfo, int nRequestID, bool bIsLast);
  virtual void OnRtnDepthMarketData(CZQThostFtdcDepthMarketDataField* pDepthMarketData);
  virtual void OnRspSubMarketData(CZQThostFtdcSpecificInstrumentField* pSpecificInstrument, CZQThostFtdcRspInfoField* pRspInfo, int nRequestID, bool bIsLast);
  virtual void OnRspUnSubMarketData(CZQThostFtdcSpecificInstrumentField* pSpecificInstrument, CZQThostFtdcRspInfoField* pRspInfo, int nRequestID, bool bIsLast);
  virtual void OnHeartBeatWarning(int nTimeLapse);
  virtual void OnRspError(CZQThostFtdcRspInfoField* pRspInfo, int nRequestID, bool bIsLast);
  virtual void OnRspUserLogin(CZQThostFtdcRspUserLoginField* pRspUserLogin, CZQThostFtdcRspInfoField* pRspInfo, int nRequestID, bool bIsLast);
  virtual void OnFrontConnected();

 private:
  PyObject * py_spi;
};

#endif
