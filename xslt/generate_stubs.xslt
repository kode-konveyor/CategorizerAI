<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE xml>
<xsl:stylesheet version="2.0"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:zenta="http://magwas.rulez.org/zenta"
	xmlns:zentatools="java:org.rulez.magwas.zentatools.XPathFunctions"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

	<xsl:output method="xml" version="1.0" encoding="utf-8"
		indent="yes" omit-xml-declaration="yes" />

	<xsl:include href="xslt/functions.xslt" />

	<xsl:param name="outputbase" />
    <xsl:variable name="doc" select="/"/>

    <xsl:function name="zenta:fullPackageName">
        <xsl:param name="doc"/>
        <xsl:param name="package"/>
        <xsl:for-each select="$package">
        <xsl:variable name="parent" select="zenta:neighbours($doc,.,'contains,2')"/>
        <xsl:value-of select="
            if(@xsi:type = 'Package')
            then
                if($parent/@xsi:type = 'Package')
                then
                    concat(string-join(zenta:fullPackageName($doc,$parent),''),'.',@name)
                else
                    @name
            else
                ''
        "/>
        </xsl:for-each>
    </xsl:function>

    <xsl:function name="zenta:artifactForBusinessObject">
        <xsl:param name="doc"/>
        <xsl:param name="object"/>
            <xsl:for-each select="zenta:neighbours($doc,$object,'has an example as/is an example of,1')">
            <artifact>
                <xsl:variable name="testData" select="zenta:neighbours($doc,.,'contains,2')[@xsi:type='TestData']"/>
                <xsl:copy-of select="@name"/>
                <xsl:attribute name="class" select="$testData/@name"/>
                <xsl:attribute name="package" select="zenta:fullPackageName($doc,zenta:neighbours($doc,$testData,'contains,2')[@xsi:type='Package'])"/>
            </artifact>
            </xsl:for-each>
    </xsl:function>

    <xsl:variable name="services">
		<xsl:for-each select="//element[@xsi:type='Service']">
            <xsl:variable name="result" select="zenta:neighbours(/,.,'results,1')"/>
            <service>
                <xsl:copy-of select="@name"/>
                <xsl:attribute name="type" select="$result/value[@ancestorName='is of/is type of']/@name"/>
                <xsl:attribute name="package" select="zenta:fullPackageName(/,zenta:neighbours(/,.,'is implemented by/implements,2;contains,2'))"/>
                <result>
                    <xsl:copy-of select="zenta:artifactForBusinessObject(/,$result)"/>
                </result>
                <xsl:for-each select="zenta:neighbours(/,.,'uses,1')">
                    <xsl:sort select="value[@ancestorName='referenced as/references']/@name"/>
                    <param>
                        <xsl:variable name="businessObject" select="zenta:neighbours($doc,.,'is/is used as parameter,1')"/>
                        <xsl:copy-of select="$businessObject/value[@ancestorName='is/is used as parameter']/@name"/>
                        <xsl:attribute name="type" select="$businessObject/value[@ancestorName='is of/is type of']/@name"/>
                        <xsl:copy-of select="zenta:artifactForBusinessObject($doc,$businessObject)"/>
                    </param>
                </xsl:for-each>
            </service>
		</xsl:for-each>
    </xsl:variable>

	<xsl:template match="/" mode="java">
        <xsl:for-each select="$services/*">
            <xsl:variable name="stubName" select="replace(@name,'Service','Stubs')"/>
<xsl:result-document href="target/generated/test/java/{string-join(tokenize(@package,'\.'),'/')}/{$stubName}.java">
package <xsl:value-of select="@package"/>

class <xsl:value-of select="$stubName"/> {

    public void behaviour() {
<xsl:if test="result/artifact">
        doReturn(<xsl:value-of select="result/artifact/concat(@class, '.', @name)"/>).when(<xsl:value-of select="@name"/>).call(<xsl:value-of select="string-join(param/artifact/concat(@class,'.',@name),', ')"/>)
</xsl:if>
    }
}
</xsl:result-document>
        </xsl:for-each>
	</xsl:template>

</xsl:stylesheet>

